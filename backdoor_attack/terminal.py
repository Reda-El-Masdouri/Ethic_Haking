# Créer un terminal avec Python

import subprocess
import os

# os.getpwd()              ---> fonction qui affiche le répértoire courant
# os.chdir('nouveau rep')  ---> pour changer le répértoire

while 1:
    commande = input(os.getcwd() + ' > ')
    if commande == "exit":
        break

    commande_split = commande.split(" ")
    if len(commande_split) == 2 and commande_split[0] == "cd":
        try:
            os.chdir(commande_split[1])
        except FileNotFoundError:
            print('Erreur: Répertoire non valide.')

    else:
        resultat = subprocess.run(commande, shell=True, capture_output=True, universal_newlines=True) # la fonction run() permet d'executer et attendre le résultat
        print(resultat.stdout)
