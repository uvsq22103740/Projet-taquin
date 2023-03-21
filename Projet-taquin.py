import tkinter as tk
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
        """Création des cases vides"""   
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
racine = tk.Tk()
"""Création de la fenêtre racine avec tkinter"""
racine.configure(bg="saddle brown")
"""On donne la couleur marron a notre arrière plan"""
jeu = Taquin(racine)
"""Création de la variable jeu"""
racine.mainloop()
"""Lancement de la boucle principale du jeu"""
