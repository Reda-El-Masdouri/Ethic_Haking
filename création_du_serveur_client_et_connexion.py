
# ------------------- Socket client ----------------


import socket
import time


HOST_IP = "127.0.0.1"
HOST_PORT = 32000
MAX_DATA_SIZE = 1024


print("Connexion au serveur", HOST_IP, ", port", HOST_PORT)
while 1:
    try:
        s = socket.socket()           # après chaque connexion echoué on crée une nouvelle socket
        s.connect((HOST_IP, HOST_PORT))                       # Cette fonction est bloquante
                                                              # Il faut lancer la socket serveur puis celle du client
                                                              # Si une seule machine est utilisée: ouvrir les deux
                                                              # scripts chacun sur une fenêtre.
    except ConnectionRefusedError:
        print("ERREUR: impossible de se connecter au serveur. Reconnexion ...")
        time.sleep(4)
    else:
        print("Connecté au serveur")
        break

recieve_data = s.recv(MAX_DATA_SIZE)   # la fonction recv possède un paramètre = la taille max des données reçues
if recieve_data:
    print(recieve_data.decode())       # les données reçues sont en binaire on les décode pour obtenir une chaine de caractères
else:
    print("Aucune data")

s.close()



