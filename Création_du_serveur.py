# socket -> communiquer entre deux machines et transporter toute sorte de données (en binaire)
#            on aura besoin d'une adresse ip et un port de communication


#                          ---------------- Principe ------------

# une machine (qui a le rôle de serveur) et une autre machine qui a le rôle du client.
#       le serveur peut accepter plusieurs connexions des clients
# ------ Etape 1:
# le serveur va écouter sur un port (il attend un client se connecter sur un port ex: 32000 (aléatoire et non utilisé))
# ------ Etape 2:
# de l'autre côté le client va se connecter au serveur (ip, port = 32000)
# ----- Etape 3:
# une fois la connexion établie: les applications entre les deux machines vont pouvoir échanger les données dans les deux
# sens: send/receive
# ------ Etape 4:
# on ferme la connexion avec la fonction close
# ----------------------- Comment ?
# 1) creer un script python pour la partie serveur (fonctions: BIND + listen + accept)
# 2) ..................................... client  (fonctions: connect)
# 3) pour envoyer les données on utilise la fonction "sendall" qui marche dans les deux sens
# 4) pour receptionner les données on utilise la fonction "RECV"
# 5) pour envoyer des chaines de caractères il faut les convertir en octet (binaire) avec les fonctions "Encode" et "Decode".


# --------------------- I) Sockets:   Script serveur ------------------
import socket
HOST_IP = "127.0.0.1"
HOST_PORT = 32000


s = socket.socket()
s.bind((HOST_IP, HOST_PORT))                     # la fonction bind prend un seul paramètre (ip, port)
                                                 # il faut choisir un port non utilisé (un random.int(10000, 65000))
s.listen()                                       # c'est une socket d'écoute 
print("Attente de connexion sur:", HOST_IP, "port:", HOST_PORT, "...")
connecxion_socket, adresse_client = s.accept()    # fonction bloquante
print("Connexion établie avec", adresse_client)

s.close()




