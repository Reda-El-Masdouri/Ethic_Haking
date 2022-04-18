
import socket
from this import d
import time
from tkinter.messagebox import NO
HOST_IP = "127.0.0.1"
HOST_PORT = 32000
MAX_DATA_SIZE = 1024

def socket_recieve_all_data(socket_p, data_len: int):
    current_data_len = 0
    total_data = None
    print("socket_recieve_all_data_len", data_len)
    while current_data_len < data_len:
        chunk_len = data_len - current_data_len
        if chunk_len > MAX_DATA_SIZE:
            chunk_len = MAX_DATA_SIZE
        data = socket_p.recv(chunk_len)
        print("  len:", len(data))
        if not data:
            return None
        if not total_data:
            total_data = data
        else:
            total_data += data
        current_data_len += len(data)  
        print("  total len:", current_data_len,"/", data_len)  
    return total_data

def socket_send_command_and_recieve_all_data(socket_p, command):
    if not command:
        return None
    socket_p.sendall(command.encode())

    header_data = socket_recieve_all_data(socket_p, 13)
    len_data = int(header_data.decode())  

    recieved_data_from_client = socket_recieve_all_data(socket_p, len_data)
    return recieved_data_from_client

s = socket.socket()
s.bind((HOST_IP, HOST_PORT))                     
s.listen()                                       
print("Attente de connexion sur:", HOST_IP, "port:", HOST_PORT, "...")
connecxion_socket, adresse_client = s.accept()    
print("Connexion établie avec", adresse_client)

while 1:
    info_data = socket_send_command_and_recieve_all_data(connecxion_socket, "infos")
    if not info_data:
        break
    commande = input(info_data.decode() + " > ")
    recieve_data = socket_recieve_all_data(connecxion_socket, commande)
    if not recieve_data:
        break
    print(recieve_data.decode())
    
s.close()
connecxion_socket.close()



