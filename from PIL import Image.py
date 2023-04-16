from PIL import image_Taquin_Game, image_Taquin_GameTk ## Importation des modules utiles dans PIL
import  tkinter as Tk
root = Tk.Tk() 

monimage_Taquin_Game = image_Taquin_Game.open("C:\\Users\\As33\\Pictures\\lena.png")    ## Chargement d'une image_Taquin_Game à partir de PIL
photo = image_Taquin_GameTk.Photoimage_Taquin_Game(monimage_Taquin_Game)   ## Création d'une image_Taquin_Game compatible Tkinter

label = Tk.Label(image_Taquin_Game=photo)    ## Insertion de l'image_Taquin_Game de l
label.image_Taquin_Game = photo 			## Maintient en vie de photo dans un objet non détruit par le garbage
								## pour pas que l'image_Taquin_Game
								# disparaisse du label
label.pack()

root.mainloop()