# 🚢 Bataille navale 🚢

## PROJET :
Voici le projet de battaille naval réalisé en python  dans le cadre de la semaine d'algorithmie de la première année de la coding factory
Venez jouez, seul ou à plusieurs à ce célèbre jeu de hasard pour passer des moment relativement amusant. 

## Installation :
installer python et le module regex
ouvrir le projet avec un logiciel acceptant python et lancer le code du fichier "main"

## Règles:
- Deux joueurs possèdent chacun une grille 10x10 sur laquelle ils placent 5 bateaux.
- Les types de bateaux et leurs tailles :
  -Porte-avions (5 cases)
  -Croiseur (4 cases)
  -Contre torpilleur (3 cases)
  -Sous-marin (3 cases)
  -Torpilleur (2 cases)
- Chaque joueur attaque une case de la grille adverse à tour de rôle.
Objectif : Couler tous les bateaux de l’adversaire en touchant toutes les cases de chaque
bateau.
Le Premier joueur à remplir l'objectif gagne la partie ! 


## Comment jouer ?
  Lancer la partie :
   Lorsqu'il est demandé de lancer la partie, rentrer y pour jouer ou n pour quitter le jeu
  
  placer les bateaux:
    le joueur 1 place ses bateaux en premier
    pour choisir un bateau, rentrer une des tailles de bateaux proposées encore disponible
    puis rentrer les deux coordonées des extremités du bateau dans le format A,1 et B,2 (ou [A-j],[1,10])
  
  Déroulement du tour : 
    Vous pouvez choisir 4 actions lors de votre tour:
      - pour afficher vos navires, rentrez 1
      - pour afficher vos tirs effectués, rentrez 2
      - pour tirer sur une case adverse et finir votre tour, rentrez 3
      - pour passer votre tour sans jouer taper 4
      
  pour tirer sur l'adversaire, une fois l'action 3 selectionnée, rentrez les coordonées de votre tir.
    Attention, vous ne pouvez pas tirer plusieurs fois au même endroit!
    
    
