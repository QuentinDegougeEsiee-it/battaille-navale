import function as f



start=input('lancer la partie ? (y/n) : ')
if start == 'n':
    exit()
else:
    jeu=True
    Tour_joueur = 1
    #placement des navires des joueurs
    print("Le joueur 1 place ses navires ! ")
    grille_bateau_j1=f.grille_vide()
    grille_attaque_j1=f.grille_vide()
    grille_bateau_j1, case_occupees_j1=f.place_bateau(grille_bateau_j1)

    print("Le joueur 2 place ses navires ! ")
    grille_bateau_j2=f.grille_vide()
    grille_attaque_j2=f.grille_vide()
    grille_bateau_j2 ,case_occupees_j2=f.place_bateau(grille_bateau_j2)

    while jeu :
        print("C'est le tour du Joueur ",Tour_joueur )
        if Tour_joueur == 1:
            grille_attaque_j1,grille_bateau_j2,case_occupees_j2 = f.attaquer(grille_attaque_j1,grille_bateau_j2,case_occupees_j2)
        f.affiche_grille(grille_bateau_j2)
        if len(case_occupees_j2)==0 :
            print("Le joueur 1 a coulé tous les navires du joueur 2 !!","\n VICTOIRE DU JOUEUR 1 !!!")
            print("FIN -----------------------------------------")
            jeu = False
        
        
        elif len(case_occupees_j1)==0:
            print("Le joueur 2 a coulé tous les navires du joueur 1 !!","\n VICTOIRE DU JOUEUR 2 !!!")
            print("FIN -----------------------------------------")
            jeu = False
        

