import tkinter as tk
"""Importer le module tkinter, appelé "tk" """
from PIL import Image, ImageTk 
"""Importation des modules utiles dans PIL"""
from tkinter import messagebox
import random as rd
"""Importer le module random pour générer le plateau aléatoirement"""
import pickle
"""Importer le module pickle pour sauvegarder et charger le plateau, cette bibliothèque permet d'enregistrer des objets python sous un format binaire"""
import requests
"""Pour télecharger une image à partir d'une URL"""
from io import BytesIO
"""BytesIO du module io sert à mettre l'image en des données binaires"""
racine = tk.Tk()
"""Création de la fenêtre racine avec bibliothèque tkinter"""
racine.title("Jeu du Taquin")

url = "https://user-images.githubusercontent.com/113627781/233841485-eb43ade1-f791-4494-b110-3d475082284a.png"
"URL du logo Taquin GAME =TG"
TG = requests.get(url)
"""image télechargée avec requests sous TG"""

def création_de_widgets():
    """Déclarer les variables globales qui seront utilisées dans les fonctions suivantes"""
    global boutons, bouton_sauvegarde, bouton_chargement, bouton_annulation, bouton_Aide, bouton_compteur, cr, image_Taquin_Game
    """Création de liste de boutons vides et la stocker dans la variable boutons"""
    boutons=[]
    """Création d'une variable pour des cases vides"""
    for ligne in range(4):
        """Création d'une ligne de 4"""
        bouton_ligne=[]
        """ on crée la variable "bouton_ligne" vide qui sera ensuite remplie"""
        for colonne in range(4):
            """ Création bouton avec la commande "bouge_case" qui sera appelée avec les paramètres "ligne" et "colonne" pour chaque bouton"""
            bouton = tk.Button(racine, bg="lemon chiffon", text="", width=9, height=6, command=lambda r=ligne, c=colonne: bouge_case(r, c), borderwidth=6, relief=tk.RAISED)
            """Le bouton est placé dans la fenêtre principale à la position [ligne][colonne] (selon les boucles "for" ci-dessus)"""
            bouton.grid(row=ligne, column=colonne)
            """Affiliation des boutons pour les lignes puis les colonnes"""
            bouton_ligne.append(bouton)
            """Ajout des boutons dans le ligne"""
        boutons.append(bouton_ligne)
        """Permet d'affilier ces boutons sur toutes les lignes du 4x4"""

    bouton_sauvegarde = tk.Button(racine, text="Sauvegarder",bg="green3", font=("Rog fonts",7),command=lambda:sauvegarde_du_jeu(), borderwidth=6, relief=tk.RAISED)
    bouton_sauvegarde.grid(row=5, column=1)
    """Création bouton pour sauvegarder le jeu avec la commande sauvegarde_du_jeu"""

    bouton_chargement = tk.Button(racine, text="Charger",bg="grey13", fg="light cyan",font=("Rog fonts",7),command=lambda:chargement_jeu(), borderwidth=6, relief=tk.RAISED)
    bouton_chargement.grid(row=5, column=2)
    """Création bouton pour charger le jeu avec la commande chargement_jeu"""

    bouton_annulation = tk.Button(racine, text="Annuler",bg="orange red", font=("Rog fonts",7),command=dernier_mouvement_annule, borderwidth=6, relief=tk.RAISED)
    bouton_annulation.grid(row=5, column=3)
    """Création bouton pour annuler le dernier mouvement avec la commande dernier_mouvement_annulé"""

    bouton_Aide = tk.Button(text="?",bg="RoyalBlue1",fg="Red2",font=('ROG Fonts', 38), command=lambda:Aide_callback(),borderwidth=6, relief=tk.RAISED)
    """Création du bouton AIDE """
    bouton_Aide.grid(row=3, column=4)

    bouton_compteur = tk.Label(racine, text="Nombre de coups",padx=20, pady=20, font = ("Rog fonts", "10"),bg="gold",borderwidth=6, relief=tk.RAISED)
    """On donne à notre bouton le texte la couleur et police"""
    bouton_compteur.grid(row=4, column=4)

    cr = tk.Label(racine, text="",padx=40, pady=20, font = ("Rog fonts", "20"),bg="gold",fg="Red",borderwidth=6, relief=tk.RAISED)
    """création  compte à rebours"""
    cr.grid(row=1, column=6)

    image_Taquin_Game = Image.open(BytesIO(TG.content))
    """Chargement d'une image à partir de PIL de BytesIO"""
    photo=ImageTk.PhotoImage(image_Taquin_Game)
    """Création d'une image compatible Tkinter"""
    Cadre_TG=tk.Label(image=photo)
    """Insertion de l'image de logo Taquin GAME"""
    Cadre_TG.image=photo
    """Maintient le logo dans un cadre pour pas qu'il disparaisse"""
    Cadre_TG.grid(row=1,column=4)
    """le logo est placé dans la grille par les coordonnées suivantes : row=1,column=4"""

def Aide_callback():
        """Fonction appelée lorsque le bouton "Aide" est cliqué"""
        message = "Bienvenue dans le Jeu du Taquin.🙂\n\n" \
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
                boutons[ligne][colonne].configure(text="", font=("Rog fonts",10))
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
     """Elle permet de revenir en arrière dans le jeu en restaurant l'état précédent du plateau
        et elle est appelée lorsque l'utilisateur veut annuler son dernier coup"""
     global tableau, précédent_tableau_existant
     """On utilise global pour informer qu'on utilise la variable tableau qui est définie à l'extérieur de la fonction """
     if précédent_tableau_existant is not None:
          """Si un état précédent a été enregistré, on le restaure et on met à jour le plateau """
          tableau = précédent_tableau_existant
          """Alors notre grille actuelle devient celle précédente"""
          renouvel_tableau(tableau)
          """On met à jour le tableau"""
          précédent_tableau_existant = None
          """La variable devient None car on a fini notre action d'annulation et la condition peut s'arreter"""
          affichage_compteur()

def vérifie_réussite():
        """Cette fonction va vérifier si l'enchainement des nombres du tableau est le schéma correct"""
        tableau_réussite = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, None]]
        """On détermine la combinaison gagnante """
        return tableau == tableau_réussite

def message_du_gagnant():
    """Cette fonction va afficher le message de victoire au joueur gagnant"""
    message_gagnant="Victoire!!!\n\n" \
                    "Félicitation tu es gagnant!"
    tk.messagebox.showinfo("Fin du jeu du Taquin", message_gagnant)
    """On réutilise la bibliothèque tkinter avec messagebox pour le message"""

def bouge_case(ligne, colonne):
    """Déplace une case donnée par ses coordonnées (ligne, colonne) vers une case vide à coté"""
    global tableau, précédent_tableau_existant
    if tableau[ligne][colonne] is None:
        """cette case est la case vide, il n'y a pas de nombre dedans, il n'y a rien à faire"""
        affichage_compteur(None)
        return 

    précédent_tableau_existant = [ligne[:] for ligne in tableau]
    """Stock l'état actuel du plateau de jeu avant de déplacer une case dans une variable"""

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
        """On vérifie si le joueur a gagné après avoir déplacé une case"""
        message_du_gagnant()
        """Si oui, on affiche le message de victoire"""
    affichage_compteur()

def affichage_compteur():
    """Modifie le texte du compteur"""
    global cpt, bouton_compteur
    cpt += 1
    bouton_compteur.config(text="+ " + str(cpt)+ " coups")
    """Le compteur affiche le nombre de coups"""

cpt = 0
cpt2 = 0

def affichage_compte_à_rebours():
    global cpt2, cr
    cpt2 += 1
    racine.after(1000, affichage_compte_à_rebours)
    """1000 est la durée en ms avant d'appeler la fonction affichage_compte_à_rebours"""
    cr.config(text= str(cpt2))

"""On ajoute le titre Jeu du Taquin"""
création_de_widgets()
"""Création des widgets"""
affichage_compte_à_rebours()
tableau = tableau_taquin()
"""Génération du plateau de jeu"""
racine.configure(bg="RoyalBlue1")
"""On donne la couleur Bleu a notre arrière plan"""
racine.mainloop()
"""Lancement de la boucle principale du jeu"""