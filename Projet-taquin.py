import tkinter as tk
"""Importer le module tkinter, appelé "tk" """
from tkinter import messagebox
import random as rd
"""Importer le module random pour générer le plateau aléatoirement"""
import pickle
"""Importer le module pickle pour sauvegarder et charger le plateau"""

def création_de_widgets():
    """Déclarer les variables globales qui seront utilisées dans les fonctions suivantes"""
    global boutons, bouton_sauvegarde, bouton_chargement, bouton_annulation
    """Création de liste de boutons vides et la stocker dans la variable boutons"""
    boutons=[]
    """Création d'une variable pour des cases vides"""
    for ligne in range(4):
        """Création d'une ligne de 4"""
        bouton_ligne=[]
        """ on crée la variable "bouton_ligne" vide qui sera ensuite remplie"""
        for colonne in range(4):
            """ Création bouton avec la commande "bouge_case" qui sera appelée avec les paramètres "ligne" et "colonne" pour chaque bouton"""
            bouton = tk.Button(racine, bg="lemon chiffon", text="", width=9, height=6, command=lambda r=ligne, c=colonne: bouge_case(r, c))
            """Le bouton est placé dans la fenêtre principale à la position [ligne][colonne] (selon les boucles "for" ci-dessus)"""
            bouton.grid(row=ligne, column=colonne)
            """Affiliation des boutons pour les lignes puis les colonnes"""
            bouton_ligne.append(bouton)
            """Ajout des boutons dans le ligne"""
        boutons.append(bouton_ligne)
        """Permet d'affilier ces boutons sur toutes les lignes du 4x4"""

    bouton_sauvegarde = tk.Button(racine, text="Sauvegarder",bg="green3", font=("Rog fonts",7),command=lambda:sauvegarde_du_jeu())
    bouton_sauvegarde.grid(row=5, column=1)
    """Création bouton pour sauvegarder le jeu avec la commande sauvegarde_du_jeu"""

    bouton_chargement = tk.Button(racine, text="Charger",bg="grey13", fg="light cyan",font=("Rog fonts",7),command=lambda:chargement_jeu())
    bouton_chargement.grid(row=5, column=2)
    """Création bouton pour charger le jeu avec la commande chargement_jeu"""

    bouton_annulation = tk.Button(racine, text="Annuler", bg="orange red", font=("Rog fonts",7),command=dernier_mouvement_annule) 
    bouton_annulation.grid(row=5, column=3)
    """Création bouton pour annuler le dernier mouvement avec la commande dernier_mouvement_annulé"""

    bouton_Aide = tk.Button(text="?",bg="RoyalBlue1",fg="Red2",font=('ROG Fonts', 38), command=lambda:Aide_callback())
    """Création du bouton AIDE """
    bouton_Aide.grid(row=8, column=10)
    
def Aide_callback():
        """Fonction appelée lorsque le bouton "Aide" est cliqué"""
        message = "Bienvenue dans le Jeu du Taquin.\n\n" \
                "Ce jeu consiste à trouver une combinaison.\n\n" \
                "Bonne chance!"
        tk.messagebox.showinfo("Aide", message)

def tableau_taquin():
    """création du tableau du taquin : va prendre aléatoirement un nombre entre 1 et 16"""
    nombres = list(range(1, 16,1))
    "prend le nombre pioché aleatoirement entre 1 et 16, pas=1"
    rd.shuffle(nombres)
    """on utilise la méthode shuffle pour mélanger la liste"""
    tableau = []
    """on créer la variable vide tableau pour y rajouter """
    nombres.append(None)
    """Ajoute "rien" a la fin de la liste, le dernier élément est vide"""
    for o in range(0, len(nombres), 4):
        """On parcourt de 4 en 4 le nombre d'élément de nombre : pour crée liste de 4 sous-listes, chacune contenant 4 éléments de la liste aléatoire"""
        ligne = nombres[o:o+4]
        """On attribut à une ligne un nombre 4 fois car une ligne est composée de 4 cases"""
        tableau.append(ligne)
        "on ajoute les lignes à tableau"
    renouvel_tableau(tableau)
    """Afficher le tableau initial dans les boutons de la fenêtre principale"""
    return tableau
    """Retourne la liste représentant le tableau initial"""

def renouvel_tableau(tableau):
    """Parcourt de chaque bouton dans la fenêtre principale"""
    for ligne in range(4):
        for colonne in range(4):
            nombre = tableau[ligne][colonne]
            """Stocke le nombre ou la valeur "None" dans la variable nombre"""
            if nombre is None:
                """Si "nombre" est "None", effacer le texte du bouton"""
                boutons[ligne][colonne].configure(text="")
            else:
                """Sinon, on écrit le nombre dans le bouton"""
                boutons[ligne][colonne].configure(text=str(nombre), font=("Rog fonts",10))
                """un nombre par case on ajoute ligne au tableau et on met une police fun de taille 20"""

def sauvegarde_du_jeu():
    """Sauvegarde l'état actuel du plateau de jeu dans un fichier binaire appelé save.dat"""
    with open("save.dat", "wb") as svg:
        pickle.dump(tableau, svg)
        """Utilisation du module pickle pour sauvegarder"""
    message_SV = "Votre partie est sauvegardée"
    tk.messagebox.showinfo("Sauvegarde", message_SV)

def chargement_jeu():
    """Charge l'état précédemment sauvegardé du plateau de jeu à partir du fichier binaire save.dat"""
    try:
        with open("save.dat", "rb") as svg:
            global tableau
            tableau = pickle.load(svg)
            """Utilisation du module pickle pour charger"""
            renouvel_tableau(tableau)
        message_CH = "Votre partie est chargée"
        tk.messagebox.showinfo("Charge", message_CH)
    except FileNotFoundError:
        """Si aucun fichier de sauvegarde n'est trouvé, affiche un message à l'utilisateur."""
        message_erreur="Aucune sauvegarde trouvée."
        print("Erreur", message_erreur)

def dernier_mouvement_annule():
     """Elle permet de revenir en arrière dans le jeu en restaurant l'état précédent du plateau et elle est appelée lorsque l'utilisateur veut annuler son dernier coup"""
     global tableau, précédent_tableau_existant
     """Si un état précédent a été enregistré, on le restaure et on met à jour le plateau """
     if précédent_tableau_existant is not None:
          tableau = précédent_tableau_existant
          renouvel_tableau(tableau)
          précédent_tableau_existant = None


def vérifie_réussite():
        """vérifie si l'enchainement des nombres du tableau est le schéma correct"""
        tableau_réussite = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, None]]
        return tableau == tableau_réussite

def message_du_gagnant():
    """Fonction qui affichera le message de victoire au joueur gagnant"""
    message_gagnant="Victoire!!!\n\n" \
                    "Félicitation tu es gagnant!"
    tk.messagebox.showinfo("Fin du jeu du Taquin", message_gagnant)
    """On réutilise la bibliothèque tkinter avec massagebox pour le message"""

def bouge_case(ligne, colonne):
    """Déplace une case donnée par ses coordonnées (ligne, colonne) vers une case vide à coté"""
    global tableau, précédent_tableau_existant
    if tableau[ligne][colonne] is None:
        """cette case est la case vide, il n'y a pas de nombre dedans, il n'y a rien à faire"""
        return  
    
    précédent_tableau_existant = [ligne[:] for ligne in tableau]
    """Enregistre l'état actuel du plateau de jeu avant de déplacer une case"""
    if ligne > 0 and tableau[ligne-1][colonne] is None:  
            """verifie si la case peut etre bougée vers le HAUT"""
            tableau[ligne-1][colonne], tableau[ligne][colonne] = tableau[ligne][colonne], tableau[ligne-1][colonne]
            renouvel_tableau(tableau)
    elif ligne < 3 and tableau[ligne+1][colonne] is None:  
            """verifie si la case peut etre bougée vers le BAS"""
            tableau[ligne+1][colonne], tableau[ligne][colonne] = tableau[ligne][colonne], tableau[ligne+1][colonne]
            renouvel_tableau(tableau)
    elif colonne > 0 and tableau[ligne][colonne-1] is None:  
            """verifie si la case peut etre bougée vers la GAUCHE"""
            tableau[ligne][colonne-1], tableau[ligne][colonne] = tableau[ligne][colonne], tableau[ligne][colonne-1]
            renouvel_tableau(tableau)
    elif colonne < 3 and tableau[ligne][colonne+1] is None:
            """verifie si la case peut etre bougée vers la DROITE"""
            tableau[ligne][colonne+1], tableau[ligne][colonne] = tableau[ligne][colonne], tableau[ligne][colonne+1]
            renouvel_tableau(tableau)
    if vérifie_réussite():
        """Vérifie si le joueur a gagné après avoir déplacé une case. Si oui, affiche un message de victoire"""
        message_du_gagnant()

racine = tk.Tk()
"""Création de la fenêtre racine avec bibliothèque tkinter"""
racine.title("Jeu du Taquin")
"""On ajoute le titre Jeu du Taquin"""
création_de_widgets()
"""Création des widgets"""
tableau = tableau_taquin()
"""Génération du plateau de jeu"""
racine.configure(bg="RoyalBlue1")
"""On donne la couleur Bleu a notre arrière plan"""
racine.mainloop()
"""Lancement de la boucle principale du jeu"""