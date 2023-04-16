# Projet-taquin!
<img width="250" alt="Taquin Game" src="https://user-images.githubusercontent.com/113627781/231962361-ee509987-7a9b-4198-b02b-b8047d13d8ae.png">

SAUVAGE Angélique 22103740

ACCES   Alexandre 22205300

OUK     Lily      22106262

GALLOIS Léa       22105352

[Projet du jeu du Taquin](https://github.com/uvsq22103740/Projet-taquin/tree/master)

_Branche Master_

---

**Abstract**

Dans ce projet, on veut programmer le jeu solitaire du taquin.
Il s’agit d’un puzzle constitué de 15 carrés numérotés de 1 à 15 qui peuvent coulisser horizontalement et verticalement à l’intérieur d’un cadre carré
qui contient un emplacement vide. Un carré ne peut coulisser que si l’emplacement voisin dans la direction choisie est vide.
L’objectif est de déplacer les carrés de manière à obtenir la configuration donnée à la figure 1.
Pour cela on utilisera une interface graphique.

---

## Notre Jeu :

Léa : on importe la bibliothèque tkinter vu en cours permettant de générer notre interface graphique

Ange : Pour commencer, nous avons créer une interface graphique

Lily : On utilise la méthode init qui est une fonction qui permet d'initialiser les attributs de la classe

Léa : Nous rajoutons le titre du jeu nommé " Jeu du taquin " grace à title puis nous créeons une grille grace a la fonction "grid" et on lui donne une largeur de 5 et les reliefs.

Ange : ligne 13 on crée la fonction création_de_widgets pour définir un cadre, dans lequel on regroupera une grille et des bouttons pour faire le socle sur lequel le joueur fera sa partie.

Léa : On a ensuite crée une variable " ligne " vide que nous allons par la suite remplir.

Alexandre: On ajoute sur la ligne 17 une variable permettant de créer les cases vides dans lesquelles nous pourrons stocker les informations du jeu dans le futur.

Lily : On crée un quadrillage 4x4

Alexandre : Dans ce quadrillage on va paramétrer chaque bouton dans lesquels nous allons stocker les informations du jeu par la suite

Alexandre : Création du bouton de sauvegarde : bouton_sauvegarde

Léa : Création du bouton de chargement : bouton_chargement

Lily : Création du bouton d'annulation : bouton_annulation

Ange : Création du bouton AIDE : bouton_Aide avec messagbox et fonction Aide_callback qui est appelée lorsque le bouton AIDE est cliqué
Ce bouton une fois cliqué, affiche un message informatif sur le jeu pour que le joueur comprenne ce qu'il doit faire.

Ange : Notre jeu repose donc sur la fonction création_de_widgets (en plus de celles des 4 boutons précédents), et sur les 9 fonctions suivantes :

- tableau_taquin            :

Ange : Création de la fonction tableau taquin, on va créer ensuite une fonction qui permetera de mettre les nombre de cette fonction dans les cases du tableau taquin
On veut faire apparaitre les nombres dans le tableau, de manière aléatoire allant de 1 à 16 avec un pas de 1.

- renouvel_tableau          :
Ange : On a créer une fonction complémentaire à tableau_taquin pour cela, la fonction renouvel_tableau qui va mettre dans les cases des nombres format str et dans celle qui a nombre is none, on met un espace "" pour montrer qu'elle est vide
On donne aussi une Police fun aux nombres pour donner un style à notre jeu!

- sauvegarde_du_jeu         :

Alexandre: On crée la fonction permettant la sauvegarde du jeu que l'on va affilier au bouton sur l'interface graphique et qui va afficher un message une fois la partie sauvegardée.

- chargement_jeu            :

- dernier_mouvement_annule  :

- vérifie_réussite          :
Ange: Quand le joueur aura réaliser le tableau gagnant [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, None]]
<img width="233" alt="Taquin résolu wikipedia" src="https://user-images.githubusercontent.com/113627781/231073188-5fd56cf4-ffc9-4b95-9d07-5c5a3d220c30.png">

On aura un message pour le joueur gagnant qui lui annonce qu'il a gagné

- message_du_gagnant        :


- bouge_case                :

Ange : On crée une fonction bouge_case qui permetra de bouger les cases, on utilise if elif

- affiche_compteur          :
Ange : Cette fonction modifie le texte du compteur.
L'instruction global cpt permet de modifier la variable globale à l'intérieur de la fonction.
Le compteur affiche le nombre de coups avec la méthode 'config()' (on modifie le paramètre du compteur)

---

## Les couleurs des boutons

Ange : Les cases prennent une couleur chacunne grace aux paramètres de choix de couleurs vu en cours:
* `fg` (ou `foreground`): couleur du texte
* `bg` (ou `background`): couleur du fond

1. sauvegarde = Vert
<img width="100" alt="sauvegarde" src="https://user-images.githubusercontent.com/113627781/230908483-2045a1f9-98f6-4a4f-b00c-e41881e5e751.png">

2. chargement = Noir
<img width="100" alt="charge" src="https://user-images.githubusercontent.com/113627781/230908501-f13c70f3-0297-419e-b174-9bbaeb8fdb95.png">

3. Annulation = Rouge orangé
<img width="100" alt="annulation" src="https://user-images.githubusercontent.com/113627781/230908540-ba57ae6b-9774-4ed8-a499-44dba52c8e65.png">

Ange : Le bouton AIDE est mis sous une forme plus pertinente pour le joueur :

<img width="100" alt="sigle" src="https://user-images.githubusercontent.com/113627781/230907726-7a2aac9f-c813-49ee-8242-4d0d6db5b4d9.png">

Ange : Création d'un compteur de coups!

<img width="163" alt="image" src="https://user-images.githubusercontent.com/113627781/231862070-b8de8a8e-e554-49a2-acf8-86991dd0ce37.png">

Ange : affichage dans la fenetre du logo du jeu _TAQUIN GAME_
<img width="55" alt="Taquin game uptated 16 32" src="https://user-images.githubusercontent.com/113627781/232315225-2eeec61c-a2d5-46bc-b568-03dfff4996e8.png">

---

**Sources**

-Pour le Readmee : https://www.freecodecamp.org/french/news/comment-ecrire-un-bon-fichier-readme/

- Pour le Logo : https://www.canva.com/design/DAFfyFwmz58/vQE6Hf8bZONutXV5sbNC7A/edit?utm_content=DAFfyFwmz58&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

- https://www.canva.com/design/DAFfyFwmz58/vQE6Hf8bZONutXV5sbNC7A/edit?utm_content=DAFfyFwmz58&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

- Le cours sur l'interface graphique "02_gui.ipynb"

- Pour afficher le logo dans la fenetre Tk https://askcodez.com/comment-ajouter-une-image-dans-tkinter.html
https://pythonpoint.net/how-to-install-pil-in-python/!

- Pour le choix des couleurs [Tableau Tkinter color charts .png](https://file%2B.vscode-resource.vscode-cdn.net/c%3A/Users/As33/Desktop/L1%20Bi/Info/S2-python-main/S2-python-main/cours/02_interface_graphique/800px-TkInterColorCharts.png?version%3D1681656888055)