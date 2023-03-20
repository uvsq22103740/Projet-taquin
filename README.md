# Projet-taquin
Abstract:
Dans ce projet, on veut programmer le jeu solitaire du taquin.
Il s’agit d’un puzzle constitué de 15 carrés numérotés de 1 à 15 qui peuvent coulisser horizontalement et verticalement à l’intérieur d’un cadre carré
qui contient un emplacement vide. Un carré ne peut coulisser que si l’emplacement voisin dans la direction choisie est vide.
L’objectif est de déplacer les carrés de manière à obtenir la configuration donnée à la figure 1.

Pour cela on utilisera une interface graphique.

Léa : on importe la bibliothèque tkinter vu en cours permettant de générer notre interface graphique

Ange : Pour commencer, nous avons créer une interface graphique, mais nous nous somme rendu compte qu'il était plus efficace de regrouper les données et des fonctionnalités dans une classe qu'on a nommé "Taquin" en l'honneur de notre petit jeu.

On a regroupé les données et des fonctionnalités dans une classe qu'on a nommé Taquin dans la ligne 3

Lily : On utilise la méthode init qui est une fonction qui permet d'initialiser les attributs de la classe

Léa : Nous rajoutons le titre du jeu nommé " Jeu du taquin " grace a la fonction title puis nous créeons une grille grace a la fonction "grid" et on lui donne une largeur de 5 et les reliefs.

Léa : On a ensuite crée une variable " ligne " vide que nous allons par la suite remplir.

Alexandre: On ajoute sur la ligne 14 une variable permettant de créer les cases vides dans lesquelles nous pourrons stocker les informations du jeu dans le futur.

Lily : On crée un quadrillage 4x4

Alexandre: Dans ce quadrillage on va paramétrer chaque bouton dans lesquels nous allons stocker les informations du jeu par la suite
