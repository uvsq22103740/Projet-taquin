import tkinter as tk
"""Importer le module tkinter, appelé "tk" """
from tkinter import messagebox
import random as rd
"""Importer le module random pour générer le plateau aléatoirement"""
import pickle
"""Importer le module pickle pour sauvegarder et charger le plateau"""

class Taquin:
    """On regroupe les données et des fonctionnalités dans une classe qu'on nomme Taquin"""
    def __init__(T, jeu):
        """On utilise la méthode init pour effectuer des opérations lors de l'instanciation de notre classe"""
        T.jeu = jeu
        jeu.title("Jeu du Taquin")
        """On ajoute le titre Jeu du Taquin"""
        T.grid = tk.Frame(jeu, borderwidth=10, relief=tk.RAISED)
        """ Création de la grille"""
        T.creation_de_widget(jeu)
        T.grid.pack()
        """permet de placer le cadre T.grid dans la fenêtre principale de jeu."""

    def creation_de_widget(T,jeu):
        T.bouton = []
        """Création d'une variable pour des cases vides"""   
        for i in range(4):
            """Création d'une ligne de 4"""
            ligne = []
            """ on crée la variable "ligne" vide qui sera ensuite remplie"""
            for j in range(4):
                """ Création bouton avec la commande "bouge_case" qui sera appelée avec les paramètres "ligne" et "colonne" pour chaque bouton"""
                bouton = tk.Button(T.grid, bg="lemon chiffon", width=9, height=6, font=('ROG Fonts', 10),command=lambda ligne=i, colonne=j: T.bouge_case(ligne, colonne))
                """Le bouton est placé dans la fenêtre principale à la position [ligne][colonne] (selon les boucles "for" ci-dessus)"""
                bouton.grid(row=i, column=j)
                """Affiliation des boutons pour les lignes puis les colonnes"""
                ligne.append(bouton)
                """Ajout des boutons dans le ligne"""
            T.bouton.append(ligne)
            """Permet d'affilier ces boutons sur toutes les lignes du 4x4"""
        T.Aide = tk.Button(jeu, text="?",bg="RoyalBlue1",fg="Red2",font=('ROG Fonts', 38), command=lambda:T.Aide_callback())
        """Création du bouton AIDE """
        T.Aide.pack(side="bottom")
        T.Sauvegarde = tk.Button(jeu, text="Sauvegarder",bg="green3",font=('ROG Fonts', 10), command=lambda:T.Sauvegarde_callback())
        """Création du bouton SAUVEGARDER """
        T.Sauvegarde.pack(side="bottom")
        T.tableau = T.tableau_taquin()
        
        bouton_chargement = tk.Button(racine, text="Charger",bg="grey13", fg="light cyan",font=("Rog fonts",7))
        bouton_chargement.pack(side="bottom")
        """Création bouton pour charger le jeu"""

        bouton_annulation = tk.Button(racine, text="Annuler",bg="orange red", font=("Rog fonts",7))
        bouton_annulation.pack(side="bottom")
        """Création bouton pour annuler le dernier mouvement"""

    def Aide_callback(T):
            """Fonction appelée lorsque le bouton "Aide" est cliqué"""
            message = "Bienvenue dans le Jeu du Taquin.\n\n" \
                    "Ce jeu consiste à trouver une combinaison.\n\n" \
                    "Bonne chance!"
            tk.messagebox.showinfo("Aide", message)
        
    def Sauvegarde_callback(T):
            """Fonction appelée lorsque le bouton "Sauvegarder" est cliqué"""
            message_SV = "Votre partie est sauvegardée"
            tk.messagebox.showinfo("Sauvegarde", message_SV)

    def tableau_taquin(T):
        """création du tableau du taquin : va prendre aléatoirement un nombre entre 1 et 16"""
        nombre=list(range(1, 16,1))
        "prend le nombre pioché aleatoirement entre 1 et 16, pas=1"
        rd.shuffle(nombre)
        """on utilise la méthode shuffle pour mélanger la liste"""
        tableau=[]
        """on créer la variable vide tableau pour y rajouter """
        nombre.append(None)
        """Ajoute "rien" a la fin de la liste, le dernier élément est vide"""
        for o in range(0, len(nombre), 4):
            """On parcourt de 4 en 4 le nombre d'élément de nombre : pour crée liste de 4 sous-listes, chacune contenant 4 éléments de la liste aléatoire"""
            ligne = nombre[o:o+4]
            """On attribut à une ligne un nombre 4 fois car une ligne est composée de 4 cases"""
            tableau.append(ligne)
            "on ajoute les lignes à tableau"
        T.renouvel_tableau(tableau)
        """Afficher le tableau initial dans les boutons de la fenêtre principale"""
        return tableau
        """Retourne la liste représentant le tableau initial"""

    def renouvel_tableau(T,tableau):
        """Parcourt de chaque bouton dans la fenêtre principale"""
        for ligne in range(4):
            for colonne in range(4):
                nombre = tableau[ligne][colonne]
                """Stocke le nombre ou la valeur "None" dans la variable nombre"""
                if nombre is None:
                    """Si "nombre" est "None", effacer le texte du bouton"""
                    T.bouton[ligne][colonne].configure(text="")    
                else:
                    """Sinon, on écrit le nombre dans le bouton"""
                    T.bouton[ligne][colonne].configure(text=str(nombre), font=("Rog fonts",10))
                    """un nombre par case on ajoute ligne au tableau et on met une police fun de taille 20"""

    def vérifie_réussite(T):
            """vérifie si l'enchainement des nombres du tableau est le schéma correct"""
            tableau_réussite = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, None]]
            return T.tableau == tableau_réussite

    def message_du_gagnant():
        """on va définir le message du gagnant"""
        message_gagnant="Victoire!!!\n\n" \
                        "Félicitation tu es gagnant!"
        tk.messagebox.showinfo("Fin du jeu du Taquin", message_gagnant)
        """On réutilise la bibliothèque tkinter avec massagebox pour le message"""

    def bouge_case(T, ligne, colonne):
        """Déplace une case donnée par ses coordonnées (ligne, colonne) vers une case vide à coté"""
        if T.tableau[ligne][colonne] is None:
            """cette case est la case vide, il n'y a pas de nombre dedans, il n'y a rien à faire"""
            return
        if ligne > 0 and T.tableau[ligne-1][colonne] is None:  
            """verifie si la case peut etre bougée vers le HAUT"""
            T.tableau[ligne-1][colonne], T.tableau[ligne][colonne] = T.tableau[ligne][colonne], T.tableau[ligne-1][colonne]
            T.renouvel_tableau(T.tableau)
        elif ligne < 3 and T.tableau[ligne+1][colonne] is None:  
            """verifie si la case peut etre bougée vers le BAS"""
            T.tableau[ligne+1][colonne], T.tableau[ligne][colonne] = T.tableau[ligne][colonne], T.tableau[ligne+1][colonne]
            T.renouvel_tableau(T.tableau)
        elif colonne > 0 and T.tableau[ligne][colonne-1] is None:  
            """verifie si la case peut etre bougée vers la GAUCHE"""
            T.tableau[ligne][colonne-1], T.tableau[ligne][colonne] = T.tableau[ligne][colonne], T.tableau[ligne][colonne-1]
            T.renouvel_tableau(T.tableau)
        elif colonne < 3 and T.tableau[ligne][colonne+1] is None:
            """verifie si la case peut etre bougée vers la DROITE"""
            T.tableau[ligne][colonne+1], T.tableau[ligne][colonne] = T.tableau[ligne][colonne], T.tableau[ligne][colonne+1]
            T.renouvel_tableau(T.tableau)
        if T.vérifie_réussite():
            """Vérifie si le joueur a gagné après avoir déplacé une case. Si oui, affiche un message de victoire"""
            T.message_du_gagnant()
    
racine = tk.Tk()
"""Création de la fenêtre racine avec bibliothèque tkinter"""
racine.configure(bg="RoyalBlue1")
"""On donne la couleur Bleu a notre arrière plan"""
jeu = Taquin(racine)
"""Création de la variable jeu"""
racine.mainloop()
"""Lancement de la boucle principale du jeu"""