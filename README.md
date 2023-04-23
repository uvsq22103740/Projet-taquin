# Projet-taquin!
<img width="250" alt="Taquin Game" src="https://user-images.githubusercontent.com/113627781/231962361-ee509987-7a9b-4198-b02b-b8047d13d8ae.png">

SAUVAGE Angélique 22103740

ACCES   Alexandre 22205300

OUK     Lily      22106262

GALLOIS Léa       22105352

[Projet du jeu du Taquin](https://github.com/uvsq22103740/Projet-taquin/tree/master)

_Branche Master_

---

## Abstract

Dans ce projet, on veut programmer le jeu solitaire du taquin.
Il s’agit d’un puzzle constitué de 15 carrés numérotés de 1 à 15 qui peuvent coulisser horizontalement et verticalement à l’intérieur d’un cadre carré
qui contient un emplacement vide. Un carré ne peut coulisser que si l’emplacement voisin dans la direction choisie est vide.
L’objectif est de déplacer les carrés de manière à obtenir la configuration donnée à la figure 1.
Pour cela on utilisera une interface graphique.

---

## Notre Jeu :

Léa : Pour commencer on importe la bibliothèque tkinter vu en cours permettant de générer notre interface graphique 

Angélique : On importe les bibliothèques Random, Image, ImageTk, Requests, pickele, BytesIO

Angélique : On donne URL du logo de notre jeu

Angélique : Notre code est composé de 12 fonctions que nous allons expliquer dans ce _Readmee_

Lily : On utilise la méthode init qui est une fonction qui permet d'initialiser les attributs de la classe

Léa : Nous rajoutons le titre du jeu nommé **" Jeu du taquin "** grace à title puis nous créeons une grille grace a "grid" et on lui donne une largeur de 5 et les reliefs.

Angélique : ligne 14 on crée la fonction **création_de_widgets** pour définir un cadre, dans lequel on regroupera une grille et des bouttons pour faire le socle sur lequel le joueur fera sa partie, selon le modèle du jeu du Taquin.

Léa : On a ensuite crée une variable " ligne " vide que nous allons par la suite remplir.

Alexandre: On ajoute sur la ligne 17 une variable permettant de créer les cases vides dans lesquelles nous pourrons stocker les informations du jeu dans le futur.

Lily : On crée un quadrillage 4x4

Alexandre : Dans ce quadrillage on va paramétrer chaque bouton dans lesquels nous allons stocker les informations du jeu par la suite

Alexandre : Création du bouton de sauvegarde : **bouton_sauvegarde**

Léa : Création du bouton de chargement : **bouton_chargement**, ce bouton nous permet de charger l'état précédemment sauvegardé du plateau de jeu.

Lily : Création du bouton d'annulation : **bouton_annulation**

Angélique : Création du bouton **AIDE** : 
**bouton_Aide** avec messagbox et fonction Aide_callback qui est appelée lorsque le bouton AIDE est cliqué
Ce bouton une fois cliqué, affiche un message informatif sur le jeu pour que le joueur comprenne ce qu'il doit faire.

Angélique : Notre jeu repose donc sur la fonction création_de_widgets (en plus de celles des 4 boutons précédents), et sur les 9 fonctions suivantes :

- **tableau_taquin**            :

Angélique : Création de la fonction tableau taquin, on va créer ensuite une fonction qui permetera de mettre les nombre de cette fonction dans les cases du tableau taquin
On veut faire apparaitre les nombres dans le tableau, de manière aléatoire allant de 1 à 16 avec un pas de 1.

- **renouvel_tableau**          :

Angélique : On a créer une fonction complémentaire à tableau_taquin pour cela, la fonction renouvel_tableau qui va mettre dans les cases des nombres format str et dans celle qui a nombre is none, on met un espace "" pour montrer qu'elle est vide
On donne aussi une Police fun aux nombres pour donner un style à notre jeu!

- **sauvegarde_du_jeu**         :

Alexandre: On crée la fonction permettant la sauvegarde du jeu que l'on va affilier au bouton sur l'interface graphique et qui va afficher un message une fois la partie sauvegardée.

- **chargement_jeu**            :

Léa :  Pour pouvoir jouer une partie et retrouver l'état, le placement, de la partie chargé précédament, nous avons crée le bouton chargement du jeu : lorsque la partie est chargée, un message s'affiche à l'utilisateur : "Votre partie est chargée" et ainsi il retrouve l'état des cases au moment du chargement.
A l'inverse, si aucun fichier de sauvegarde n'est trouvé, un message s'affiche à l'utilisateur : "Aucune sauvegarde trouvée."

- **dernier_mouvement_annule**  :

Lily : Pour annuler un déplacement, on a crée une fonction qui va annuler le dernier mouvement effectué, ainsi le jeu va afficher la grille obtenue avant celui-ci. Cette fonction est associée au bouton annulation.

- **vérifie_réussite**  

Lily : On crée une fonction qui va vérifier la combinaison gagnante suivante : [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, None]]
La combinaison gagnante correspond à l'emplacement des cases sur l'image suivante : 

<img width="233" alt="Taquin résolu wikipedia" src="https://user-images.githubusercontent.com/113627781/231073188-5fd56cf4-ffc9-4b95-9d07-5c5a3d220c30.png">

Un message va s'afficher pour le joueur gagnant 

- **message_du_gagnant**        :

Lily : On crée un message qui s'affiche lorsque le jeu est gagné : "Victoire !!!", "Félicitation tu es gagnant !" 

- **bouge_case**                :

Angélique : On crée une fonction bouge_case qui permetra de bouger les cases, on utilise if elif

- **affiche_compteur**          :

Angélique : Cette fonction modifie le texte du compteur.
L'instruction global cpt permet de modifier la variable globale à l'intérieur de la fonction.
Le compteur affiche le nombre de coups avec la méthode 'config()' (on modifie le paramètre du compteur)

- **affichage_compte_à_rebours** :

Angélique : Cette fonction modifie le texte du label cr et donne le temps depuis le lancement du jeu.
Le compte à rebours affiche le temps avec la méthode 'config()' : 1000 est la durée en ms avant d'appeler la fonction affichage_compte_à_rebours.

---

## Les couleurs des boutons

Angélique : Les cases prennent une couleur chacunne grace aux paramètres de choix de couleurs vu en cours:
* `fg` (ou `foreground`): couleur du texte
* `bg` (ou `background`): couleur du fond

1. sauvegarde = Vert
<img width="100" alt="sauvegarde" src="https://user-images.githubusercontent.com/113627781/230908483-2045a1f9-98f6-4a4f-b00c-e41881e5e751.png">

2. chargement = Noir
<img width="100" alt="charge" src="https://user-images.githubusercontent.com/113627781/230908501-f13c70f3-0297-419e-b174-9bbaeb8fdb95.png">

3. Annulation = Rouge orangé
<img width="100" alt="annulation" src="https://user-images.githubusercontent.com/113627781/230908540-ba57ae6b-9774-4ed8-a499-44dba52c8e65.png">

Angélique : Le bouton AIDE est mis sous une forme plus pertinente pour le joueur :

<img width="100" alt="sigle" src="https://user-images.githubusercontent.com/113627781/230907726-7a2aac9f-c813-49ee-8242-4d0d6db5b4d9.png">

Angélique : Création d'un compteur de coups!

<img width="163" alt="image" src="https://user-images.githubusercontent.com/113627781/231862070-b8de8a8e-e554-49a2-acf8-86991dd0ce37.png">

Angélique : Création d'un compteur de temps (CR en ms):

<img width="287" alt="Taquin CR" src="https://user-images.githubusercontent.com/113627781/233839447-eea9df09-4f35-4c45-9839-b3b533859278.png">

Angélique : affichage dans la fenetre du logo du jeu _TAQUIN GAME_
<img width="55" alt="Taquin game uptated 16 32" src="https://user-images.githubusercontent.com/113627781/232315225-2eeec61c-a2d5-46bc-b568-03dfff4996e8.png">
On utilise l'url, tout le monde peut trouver l'image par ce lien!
On charge l'image à partir de PIL de BytesIO.
On crée une image compatible Tkinter.
On insert l'image de logo Taquin GAME.
On maintient le logo dans un cadre pour pas qu'il disparaisse (cadre_TG) puis le logo est placé dans la grille par les coordonnées suivantes : row=1,column=4  
[Logo Taquin GAME](https://user-images.githubusercontent.com/113627781/232315225-2eeec61c-a2d5-46bc-b568-03dfff4996e8.png)


---

## Nos Sources

- Pour le Readmee : https://www.freecodecamp.org/french/news/comment-ecrire-un-bon-fichier-readme/

- Pour le Logo : https://www.canva.com/design/DAFfyFwmz58/vQE6Hf8bZONutXV5sbNC7A/edit?utm_content=DAFfyFwmz58&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

- https://www.canva.com/design/DAFfyFwmz58/vQE6Hf8bZONutXV5sbNC7A/edit?utm_content=DAFfyFwmz58&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

- Le cours sur l'interface graphique "02_gui.ipynb"

- Pour afficher le logo dans la fenetre Tk https://askcodez.com/comment-ajouter-une-image-dans-tkinter.html
https://pythonpoint.net/how-to-install-pil-in-python/!

- Pour le choix des couleurs

Tableau Tkinter des couleurs ![800px-TkInterColorCharts](https://user-images.githubusercontent.com/113627781/233839713-152a9549-2bf6-44ad-b83d-e37f19252299.png)


Extrait de `http://stackoverflow.com/questions/4969543/colour-chart-for-tkinter-and-tix-using-python`