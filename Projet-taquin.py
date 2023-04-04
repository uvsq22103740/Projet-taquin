import tkinter as tk
from tkinter import messagebox
import random as rd
"""importation de la bibliothèque tkinter et random"""

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
                """Création des boutons avec lesquels le joueur pourra interagir par l'avenir"""
                bouton = tk.Button(T.grid, width=8, height=4, font=('ROG Fonts', 20),command=lambda ligne=i, colonne=j: T.bouge_case(ligne, colonne))
                """Apparition du bouton sur l'interface graphique + on appelle la fonction bouge_case"""
                bouton.grid(row=i, column=j)
                """Affiliation des boutons pour les lignes puis les colonnes"""
                ligne.append(bouton)
                """Ajout des boutons dans le ligne"""
            T.bouton.append(ligne)
            """Permet d'affilier ces boutons sur toutes les lignes du 4x4"""
        T.Aide = tk.Button(jeu, text="Aide",fg="RoyalBlue1",font=('ROG Fonts', 8), command=lambda:T.Aide_callback())
        """Création du bouton AIDE """
        T.Aide.pack(side="bottom")
        T.Sauvegarde = tk.Button(jeu, text="Sauvegarder",fg="orange red",font=('ROG Fonts', 10), command=lambda:T.Sauvegarde_callback())
        """Création du bouton SAUVEGARDER """
        T.Sauvegarde.pack(side="bottom")
        T.tableau = T.tableau_taquin()
    
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
        "prend le nombre pioché aleatoirement entre 1 et 16"
        rd.shuffle(nombre)
        """on utilise la méthode shuffle pour mélanger la liste"""
        tableau=[]
        """on créer la variable vide tableau pour y rajouter """
        nombre.append(None)
        """Ajoute "rien" a la fin de la liste, le dernier élément est vide"""
        for o in range(0, len(nombre), 4):
            """On parcourt de 4 en 4 le nombre d'élément de nombre"""
            ligne = nombre[o:o+4]
            """On attribut à une ligne un nombre 4 fois car une ligne est composée de 4 cases"""
            tableau.append(ligne)
        T.renouvel_tableau(tableau)
        return tableau
        """retourne le tableau de la fonction"""

    def renouvel_tableau(T,tableau):
        for ligne in range(4):
            for colonne in range(4):
                nombre = tableau[ligne][colonne]
                if nombre is None:
                    T.bouton[ligne][colonne].configure(text="")
                    """cette case est la case vide, il n'y a pas de nombre dedans"""
                else:
                    T.bouton[ligne][colonne].configure(text=str(nombre), font=("Rog fonts",20))
                    """un nombre par case on ajoute ligne au tableau et on met une police fun de taille 20"""

    def bouge_case(T, ligne, colonne):
        """on veut bouger les cases"""
        if T.tableau[ligne][colonne] is None:
            return
        """verifie si la case peut etre bougée"""
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

    def vérifie_réussite(T):
        tableau_réussite = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, None]]
        return t.tableau == tableau_réussite
    
racine = tk.Tk()
"""Création de la fenêtre racine avec bibliothèque tkinter"""
racine.configure(bg="RoyalBlue1")
"""On donne la couleur Bleu a notre arrière plan"""
jeu = Taquin(racine)
"""Création de la variable jeu"""
racine.mainloop()
"""Lancement de la boucle principale du jeu"""