import tkinter as tk
"""importation de la bibliothèque tkinter"""
class Taquin:
    """On regroupe les données et des fonctionnalités dans une classe qu'on nomme Taquin"""
    def __init__(T, jeu):
        """On utilise la méthode init pour effectuer des opérations lors de l'instanciation de notre classe"""
        T.jeu = jeu
        jeu.title("Jeu du Taquin")
        """On ajoute le titre Jeu du Taquin"""
        T.grid = tk.Frame(jeu, borderwidth=5, relief="solid")
        """ Création de la grille"""
        T.grid.pack()
        """permet de placer le cadre T.grid dans la fenêtre principale de jeu."""

racine = tk.Tk()
"""Création de la fenêtre racine"""
jeu = Taquin(racine)
racine.mainloop()
"""Lancement de la boucle principale"""