
import socket
from this import d
import time
from tkinter.messagebox import NO
HOST_IP = "127.0.0.1"
HOST_PORT = 32000
MAX_DATA_SIZE = 1024

def socket_recieve_all_data(socket_p, data_len):
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

s = socket.socket()
s.bind((HOST_IP, HOST_PORT))                     
s.listen()                                       
print("Attente de connexion sur:", HOST_IP, "port:", HOST_PORT, "...")
connecxion_socket, adresse_client = s.accept()    
print("Connexion établie avec", adresse_client)

while 1:
    commande = input("Commande: ")
    if commande == "":
        continue
    connecxion_socket.sendall(commande.encode())

    header_data = socket_recieve_all_data(connecxion_socket, 13)
    len_data = int(header_data.decode())  

    recieved_data_from_client = socket_recieve_all_data(connecxion_socket, len_data)
    print("len_data:", len_data)
    if recieved_data_from_client:
        print(recieved_data_from_client.decode())
    else:
        break
s.close()
connecxion_socket.close()



