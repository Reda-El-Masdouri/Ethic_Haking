
import socket
import time
HOST_IP = "127.0.0.1"
HOST_PORT = 32000
MAX_DATA_SIZE = 1024

s = socket.socket()
s.bind((HOST_IP, HOST_PORT))                     
s.listen()                                       
print("Attente de connexion sur:", HOST_IP, "port:", HOST_PORT, "...")
connecxion_socket, adresse_client = s.accept()    
print("Connexion établie avec", adresse_client)

while 1:
    commande = input("Commande: ")
    connecxion_socket.sendall(commande.encode())   
    recieved_data_from_client = connecxion_socket.recv(MAX_DATA_SIZE)
    if recieved_data_from_client:
        print(recieved_data_from_client.decode())
    else:
        break
s.close()
connecxion_socket.close()



