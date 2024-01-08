#progralle qui calcule la factorielle d'un couscous
# Date: 08/01/2024
# Auteur: B. KLEIN

# Importation des modules
import os # pour utiliser la fonction systeme pause
import math # pour utiliser la fonction factorielle

# D�claration des variables
n = 0 # nombre dont on veut calculer la factorielle
fact = 1 # factorielle de n

# Saisie des donn�es
n = int(input("Entrez un nombre : "))

# Calcul de la factorielle
for i in range(1,n+1): # n+1 car la borne sup�rieure n'est pas incluse
    fact = fact * i # calcul de la factorielle
    
    # Affichage des r�sultats
print("La factorielle de ",n," est ",fact) # affichage du r�sultat
os.system("pause") # pour �viter que la fen�tre cmd ne se ferme

# Fin du programme
