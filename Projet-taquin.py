import tkinter as tk
from tkinter import messagebox

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
            
    def apropos_bouton_callback(T):
            """Fonction appelée lorsque le bouton "À propos" est cliqué"""
            message = "Bienvenue dans le Jeu du Taquin.\n\n" \
                    "Ce jeu consiste à trouver une combinaison.\n\n" \
                    "C'est un puzzle constitué de 15 carrés numérotés de 1 à 15 qui peuvent coulisser horizontalement et verticalement à l’intérieur d’un cadre carré qui contient un emplacement vide"
            tk.messagebox.showinfo("À propos", message)
            """message descriptif informatif"""
racine = tk.Tk()
"""Création de la fenêtre racine avec bibliothèque tkinter"""
racine.configure(bg="orange red")
"""On donne la couleur marron a notre arrière plan"""
jeu = Taquin(racine)
"""Création de la variable jeu"""
racine.mainloop()
"""Lancement de la boucle principale du jeu"""