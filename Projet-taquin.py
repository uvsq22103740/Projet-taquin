import tkinter as tk
from tkinter import messagebox
import random as rd

"""importation de la bibliothèque tkinter"""
class Taquin:
    """On regroupe les données et des fonctionnalités dans une classe qu'on nomme Taquin"""
    def __init__(T, jeu):
        """On utilise la méthode init pour effectuer des opérations lors de l'instanciation de notre classe"""
        T.jeu = jeu
        jeu.title("Jeu du Taquin")
        """On ajoute le titre Jeu du Taquin"""
        T.grid = tk.Frame(jeu, borderwidth=10, relief=tk.RAISED)
        """ Création de la grille"""
        T.grid.pack()
        """permet de placer le cadre T.grid dans la fenêtre principale de jeu."""
        T.bouton = []
        """Création d'une variable pour des cases vides"""   
        for i in range(4):
            """Création d'une ligne de 4"""
            ligne = []
            """ on crée la variable "ligne" vide qui sera ensuite remplie"""
            for j in range(4):
                """Création des boutons avec lesquels le joueur pourra interagir par l'avenir"""
                bouton = tk.Button(T.grid, width=8, height=4, font=('ROG Fonts', 20))
                """Apparition du bouton sur l'interface graphique"""
                bouton.grid(row=i, column=j)
                """Affiliation des boutons pour les lignes puis les colonnes"""
                ligne.append(bouton)
                """Ajout des boutons dans le ligne"""
            T.bouton.append(ligne)
            """Permet d'affilier ces boutons sur toutes les lignes du 4x4"""
            T.apropos_bouton = tk.Button(jeu, text="À propos", command=lambda:T.apropos_bouton_callback())
            """Création du bouton À propos """
            T.apropos_bouton.pack(side="bottom")
        T.tableau = T.tableau_taquin()
            
    def apropos_bouton_callback(T):
            """Fonction appelée lorsque le bouton "À propos" est cliqué"""
            message = "Bienvenue dans le Jeu du Taquin.\n\n" \
                    "Ce jeu consiste à trouver une combinaison.\n\n" \
                    "Bonne chance!"
            tk.messagebox.showinfo("À propos", message)

    def tableau_taquin(T):
        """création du tableau du taquin : va prendre aléatoirement un nombre entre 1 et 16"""
        nombre=list(range(1, 16))
        rd.shuffle(nombre)
        tableau=[]
        """on créer la variable vide tableau pour y rajouter """
        nombre.append(None)
        for o in range(0, len(nombre), 4):
            """On parcourt de 4 en 4 le nombre d'élément de nombre"""
            ligne = nombre[o:o+4]
            """On attribut à une ligne un nombre 4 fois car une ligne est composée de 4 cases"""
            tableau.append(ligne)
        T.renouvel_tableau(tableau)#on crera demain la fonction renouvel tableau pour mettre les chiffre dans les cases
        return tableau
        """retourne le tableau de la fonction"""
        
racine = tk.Tk()
"""Création de la fenêtre racine avec bibliothèque tkinter"""
racine.configure(bg="RoyalBlue1")
"""On donne la couleur marron a notre arrière plan"""
jeu = Taquin(racine)
"""Création de la variable jeu"""
racine.mainloop()
"""Lancement de la boucle principale du jeu"""