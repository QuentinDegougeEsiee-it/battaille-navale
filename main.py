import function as f
import re




start=input('lancer la partie ? (y/n) : ')
if start == 'n':
    exit()
else:
    jeu=True
    Tour_joueur = 1
    patern_réponse = r"^[1-3]$"

    #placement des navires des joueurs
    print("Le joueur 1 place ses navires ! \n")
    grille_bateau_j1=f.grille_vide()
    grille_attaque_j1=f.grille_vide()
    grille_bateau_j1, case_occupees_j1=f.place_bateau(grille_bateau_j1)
    
    print("Le joueur 2 place ses navires ! \n")
    grille_bateau_j2=f.grille_vide()
    grille_attaque_j2=f.grille_vide()
    grille_bateau_j2 ,case_occupees_j2=f.place_bateau(grille_bateau_j2)

    #début de la partie
    while jeu :
        print("C'est le tour du Joueur ",Tour_joueur,"\n" )
        if Tour_joueur == 1:
            Tour_joueur = f.suivant(Tour_joueur)
            tir_effectuee = False
            while tir_effectuee is False:
                valid_patern = False
                while valid_patern is False:
                    #propose les actions disponibles au joueur
                    print(" Vous avez 3 actions disponible : \n - 1 : afficher vos navires \n - 2 : afficher vos tirs \n - 3 : attaquer l'adversaire \n")
                    action = input("Quelle action voulez vous effectuer  ? (1,2 ou 3) : ")
                    if re.match(patern_réponse,action):
                        valid_patern = True
                    else:
                        print("Votre réponse n'est pas valide, elle doit être  1 ,2 ou 3 . \n ")
                #affiche la grille des bateau du joueur
                if action == '1' :
                    f.affiche_grille(grille_bateau_j1)
                    print("Voici vos navires")
                #affiche la grille des tirs du joueur
                elif action == '2' :
                    f.affiche_grille(grille_attaque_j1)
                    print("Voici vos tirs")
                #fait tirer le joueur et finit son tour
                else :
                    grille_attaque_j1,grille_bateau_j2,case_occupees_j2 = f.attaquer(grille_attaque_j1,grille_bateau_j2,case_occupees_j2)
                    tir_effectuee = True
                    
        


        else:
            Tour_joueur = f.suivant(Tour_joueur)
            tir_effectuee = False
            while tir_effectuee is False:
                valid_patern = False
                while valid_patern is False:
                    #propose les actions disponibles au joueur
                    print(" Vous avez 3 actions disponible : \n - 1 : afficher vos navires \n - 2 : afficher vos tirs \n - 3 : attaquer l'adversaire \n")
                    action = input("Quelle action voulez vous effectuer  ? (1,2 ou 3) : ")
                    if re.match(patern_réponse,action):
                        valid_patern = True
                    else:
                        print("Votre réponse n'est pas valide, elle doit être  1 ,2 ou 3 . \n ")
                #affiche la grille des bateau du joueur
                if action == '1' :
                    f.affiche_grille(grille_bateau_j2)
                    print("Voici vos navires")
                #affiche la grille des tirs du joueur
                elif action == '2' :
                    f.affiche_grille(grille_attaque_j2)
                    print("Voici vos tirs")
                #fait tirer le joueur et finit son tour
                else :
                    grille_attaque_j2,grille_bateau_j1,case_occupees_j1 = f.attaquer(grille_attaque_j2,grille_bateau_j1,case_occupees_j1)
                    tir_effectuee = True

        #vérifie qu'il reste des bateaux à chaque joueur, si ce n'est pas le cas , finit la partie        
        if len(case_occupees_j2)==0 :
            print("Le joueur 1 a coulé tous les navires du joueur 2 !!","\n VICTOIRE DU JOUEUR 1 !!!\n")
            print("FIN -----------------------------------------")
            jeu = False
        elif len(case_occupees_j1)==0:
            print("Le joueur 2 a coulé tous les navires du joueur 1 !!","\n VICTOIRE DU JOUEUR 2 !!!\n")
            print("FIN -----------------------------------------")
            jeu = False

        

