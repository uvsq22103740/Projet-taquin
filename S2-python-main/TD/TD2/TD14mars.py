import tkinter as tk
racine = tk.Tk() # Création de la fenêtre racine
racine.title("affichage") # ajoute un titre
label = tk.Label(racine, text="affichage", font=("helvetica", "20")) # création du widget
label.grid() # positionnement du widget.
label.config(text="Jeu du Taquin", bg="saddle brown") # modification des paramètres du widget
racine.mainloop() # Lancement de la boucle principale
from tkinter import *

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400

if __name__ == '__main__':
    root = Tk()

    canvas = Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

    # Début de votre code
    x0 = 100
    x1 = CANVAS_WIDTH - 100
    y = CANVAS_HEIGHT / 2
    canvas.create_line(x0, y, x1, y)
    canvas.create_oval(x0 - 50, y + 50, x0 + 50, y - 50)
    canvas.create_oval(x1 - 50, y + 50, x1 + 50, y - 50)
    canvas.create_oval((x0 + x1) / 2 - 50, y + 50, (x0 + x1) / 2 + 50, y - 50)
    
    # Fin de votre code

    canvas.pack()
    root.mainloop()