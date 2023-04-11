# Projet-taquin
BI TD01

SAUVAGE Angélique 22103740

ACCES   Alexandre 22205300

OUK     Lily      22106262

GALLOIS Léa       22105352

Projet du jeu du Taquin : https://github.com/uvsq22103740/Projet-taquin/tree/master

_Branche Master_

*Abstract :

Dans ce projet, on veut programmer le jeu solitaire du taquin.
Il s’agit d’un puzzle constitué de 15 carrés numérotés de 1 à 15 qui peuvent coulisser horizontalement et verticalement à l’intérieur d’un cadre carré
qui contient un emplacement vide. Un carré ne peut coulisser que si l’emplacement voisin dans la direction choisie est vide.
L’objectif est de déplacer les carrés de manière à obtenir la configuration donnée à la figure 1.
Pour cela on utilisera une interface graphique.*

[file:///C:/Users/As33/Desktop/L1%20Bi/Info/Le%20projet/taquin.pdf](url)

Léa : on importe la bibliothèque tkinter vu en cours permettant de générer notre interface graphique

Ange : Pour commencer, nous avons créer une interface graphique

Lily : On utilise la méthode init qui est une fonction qui permet d'initialiser les attributs de la classe

Léa : Nous rajoutons le titre du jeu nommé " Jeu du taquin " grace a la fonction title puis nous créeons une grille grace a la fonction "grid" et on lui donne une largeur de 5 et les reliefs.

Ange : ligne 9 on crée la fonction création_de_widgets pour définir un cadre, dans lequel on regroupera une grille et des bouttons pour faire le socle sur lequel le joueur fera sa partie.

Léa : On a ensuite crée une variable " ligne " vide que nous allons par la suite remplir.

Alexandre: On ajoute sur la ligne 14 une variable permettant de créer les cases vides dans lesquelles nous pourrons stocker les informations du jeu dans le futur.

Lily : On crée un quadrillage 4x4

Alexandre : Dans ce quadrillage on va paramétrer chaque bouton dans lesquels nous allons stocker les informations du jeu par la suite

Ange : Création du bouton à propos avec messagbox et fonction Aide_callback qui est appelée lorsque le bouton AIDE est cliqué
Ce bouton une fois cliqué, affiche un message informatif sur le jeu pour que le joueur comprenne ce qu'il doit faire.

Ange : Création de la fonction tableau taquin, on va créer ensuite une fonction qui permetera de mettre les nombre de cette fonction dans les cases du tableau taquin

Ange : On veut faire apparaitre les nombres dans le tableau, de manière aléatoire allant de 1 à 16 avec un pas de 1.
on a créer une fonction complémentaire à tableau_taquin pour cela, la fonction renouvel_tableau qui va mettre dans les cases des nombres format str et dans celle qui a nombre is none, on met un espace "" pour montrer qu'elle est vide
On donne aussi une Police fun aux nombres pour donner un style à notre jeu!

On crée une fonction bouge_case qui permetra de bouger les cases, on utilise if elif

Ange: Quand le joueur aura réaliser le tableau gagnant [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, None]]
<img width="233" alt="Taquin résolu wikipedia" src="https://user-images.githubusercontent.com/113627781/231073188-5fd56cf4-ffc9-4b95-9d07-5c5a3d220c30.png">

On aura un message pour le joueur gagnant qui lui annonce qu'il a gagné

Ange : Les cases prennent une couleur chacunne : 

1. sauvegarde = Vert
<img width="74" alt="sauvegarde" src="https://user-images.githubusercontent.com/113627781/230908483-2045a1f9-98f6-4a4f-b00c-e41881e5e751.png">

2. chargement = Noir
<img width="50" alt="charge" src="https://user-images.githubusercontent.com/113627781/230908501-f13c70f3-0297-419e-b174-9bbaeb8fdb95.png">

3. Annulation = Rouge orangé
<img width="49" alt="annulation" src="https://user-images.githubusercontent.com/113627781/230908540-ba57ae6b-9774-4ed8-a499-44dba52c8e65.png">

Le bouton AIDE est mis sous une forme plus pertinente pour le joueur :

<img width="97" alt="sigle" src="https://user-images.githubusercontent.com/113627781/230907726-7a2aac9f-c813-49ee-8242-4d0d6db5b4d9.png">