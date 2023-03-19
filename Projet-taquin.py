import tkinter as tk

class Taquin:
    """On regroupe les données et des fonctionnalités dans une classe qu'on nomme Taquin"""
    def __init__(T, jeu):
        T.jeu = jeu
        jeu.title("Jeu du Taquin")
        """On utilise la méthode init pour effectuer des opérations lors de l'instanciation de notre classe"""
        T.grid = tk.Frame(jeu, borderwidth=5, relief="solid")
        """ Création de la grille"""
        T.grid.pack()
        """permet de placer le cadre T.grid dans la fenêtre principale de jeu."""

racine = tk.Tk()
jeu = Taquin(racine)
racine.mainloop()