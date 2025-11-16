import function as f
import re
import json
import os




start=input('lancer la partie ? (y/n) : ')
if start == 'n':
    exit()
else:
    Tour_joueur = 1
    patern_réponse = r"^[1-5]$"
    patern_jeu = r"^[1-2]$"
    choix_mode = False
    #choix du mode PVP ou PVE
    while choix_mode is False:
        print("Vous avez deux modes de jeu auquel vous pouvez jouer : \n - 1 : jeu multijoueur, vous jouez contre un autre joueur \n - 2 : jeu solo, vous jouez contre une IA\n")
        mode_de_jeu = input("À quel mode souhaitez vous jouer ? (1 ou 2) : ")
        if re.match(patern_jeu,mode_de_jeu):
            choix_mode = True
        else:
            print("Votre réponse n'est pas valide, elle doit être  1 ou 2 . \n ")
        



    #si mode de jeu duo choisi :
    if mode_de_jeu == 1 :
            #placement des navires des joueurs
        print("Le joueur 1 place ses navires ! \n")
        grille_bateau_j1=f.grille_vide()
        grille_attaque_j1=f.grille_vide()
        grille_bateau_j1, cases_occupees_j1=f.place_bateau(grille_bateau_j1)    

        print("Le joueur 2 place ses navires ! \n")
        grille_bateau_j2=f.grille_vide()
        grille_attaque_j2=f.grille_vide()
        grille_bateau_j2, cases_occupees_j2=f.place_bateau(grille_bateau_j2)
        jeu_duo = True   
        jeu_solo=False

    #si mode de jeu solo choisi :
    else:
        if os.path.exists("liste_bateaux_joueur.json"):
            charge_save= input("Une sauvegarde a été détecté, voulez-vous la charger ? y/n : ")
            if charge_save == "n":
                    #placement des navires des joueurs
                print("Le joueur 1 place ses navires ! \n")
                grille_bateau_j1=f.grille_vide()
                grille_attaque_j1=f.grille_vide()
                grille_bateau_j1, cases_occupees_j1=f.place_bateau(grille_bateau_j1)

                grille_bateau_IA = f.grille_vide()
                grille_bateau_IA, cases_occupees_IA=f.place_IA(grille_bateau_IA)
                #crée une liste de toute les coordonées dans lesquels l'IA n'as pas déjà tiré
                tirs_dispo=[]
                for ligne in range(10):
                    for colonne in range(10):
                        tirs_dispo.append((ligne,colonne))
                jeu_solo=True
                jeu_duo=False
            else: 
                with open("liste_bateaux_joueur.json","r") as bj:
                    grille_bateau_j1 = json.load(bj)
                with open("liste_bateaux_IA.json","r") as bia:
                    grille_bateau_IA = json.load(bia)
                with open("liste_Tirs_joueur.json","r") as tj:
                    grille_attaque_j1 = json.load(tj)
                with open("liste_Tirs_IA.json","r") as tia:
                    tirs_dispo = json.load(tia)
                with open("cases_occupées_joueur.json","r") as coj:
                    cases_occupees_j1 = json.load(coj)
                with open("cases_occupées_IA.json","r") as coia:
                    cases_occupees_IA = json.load(coia)
                jeu_solo=True
                jeu_duo=False
        

        else:
            #placement des navires des joueurs
            print("Le joueur 1 place ses navires ! \n")
            grille_bateau_j1=f.grille_vide()
            grille_attaque_j1=f.grille_vide()
            grille_bateau_j1, cases_occupees_j1=f.place_bateau(grille_bateau_j1)

            grille_bateau_IA = f.grille_vide()
            grille_bateau_IA, cases_occupees_IA=f.place_IA(grille_bateau_IA)
            #crée une liste de toute les coordonées dans lesquels l'IA n'as pas déjà tiré
            tirs_dispo=[]
            for ligne in range(10):
                for colonne in range(10):
                    tirs_dispo.append((ligne,colonne))
            jeu_solo=True
            jeu_duo=False




    #début de la partie duo
    while jeu_duo :
        print("C'est le tour du Joueur ",Tour_joueur,"\n" )
        if Tour_joueur == 1:
            Tour_joueur = f.suivant(Tour_joueur)
            tir_effectuee = False
            while tir_effectuee is False:
                valid_patern = False
                while valid_patern is False:
                    #propose les actions disponibles au joueur
                    print(" Vous avez 5 actions disponible : \n - 1 : afficher vos navires \n - 2 : afficher vos tirs \n - 3 : attaquer l'adversaire \n - 4 : vous passez votre tour\n - 5 : Sauvegarder et quitter la partie\n")
                    action = input("Quelle action voulez vous effectuer  ? (1, 2, 3 ou 4) : ")
                    if re.match(patern_réponse,action):
                        valid_patern = True
                    else:
                        print("Votre réponse n'est pas valide, elle doit être 1, 2, 3 ou 4 . \n ")
                #affiche la grille des bateau du joueur
                if action == '1' :
                    f.affiche_grille(grille_bateau_j1)
                    print("Voici vos navires")
                #affiche la grille des tirs du joueur
                elif action == '2' :
                    f.affiche_grille(grille_attaque_j1)
                    print("Voici vos tirs")
                #passe le tour
                elif action =='4':
                    print("Vous passez votre Tour\n")
                    tir_effectuee= True

                #fait tirer le joueur et finit son tour
                else :
                    grille_attaque_j1,grille_bateau_j2,cases_occupees_j2 = f.attaquer(grille_attaque_j1,grille_bateau_j2,cases_occupees_j2)
                    tir_effectuee = True
                    
        


        else:
            Tour_joueur = f.suivant(Tour_joueur)
            tir_effectuee = False
            while tir_effectuee is False:
                valid_patern = False
                while valid_patern is False:
                    #propose les actions disponibles au joueur
                    print("Vous avez 5 actions disponible : \n - 1 : afficher vos navires \n - 2 : afficher vos tirs \n - 3 : attaquer l'adversaire \n - 4 : vous passez votre tour\n - 5 : Sauvegarder et quitter la partie\n")
                    if re.match(patern_réponse,action):
                        valid_patern = True
                    else:
                        print("Votre réponse n'est pas valide, elle doit être  1, 2, 3 ou 4 . \n ")
                #affiche la grille des bateau du joueur
                if action == '1' :
                    f.affiche_grille(grille_bateau_j2)
                    print("Voici vos navires")
                #affiche la grille des tirs du joueur
                elif action == '2' :
                    f.affiche_grille(grille_attaque_j2)
                    print("Voici vos tirs")
                #passe le tour
                elif action =='4':
                    print("Vous passez votre Tour\n")
                    tir_effectuee= True
                elif action =='5':
                    f.save_bateaux_joueur(grille_bateau_j1)
                    exit()
                #fait tirer le joueur et finit son tour
                else :
                    grille_attaque_j2,grille_bateau_j1,cases_occupees_j1 = f.attaquer(grille_attaque_j2,grille_bateau_j1,cases_occupees_j1)
                    tir_effectuee = True

        #vérifie qu'il reste des bateaux à chaque joueur, si ce n'est pas le cas , finit la partie        
        if len(cases_occupees_j2)==0 :
            print("Le joueur 1 a coulé tous les navires du joueur 2 !!","\n VICTOIRE DU JOUEUR 1 !!!\n")
            print("FIN -----------------------------------------")
            jeu_duo = False
        elif len(cases_occupees_j1)==0:
            print("Le joueur 2 a coulé tous les navires du joueur 1 !!","\n VICTOIRE DU JOUEUR 2 !!!\n")
            print("FIN -----------------------------------------")
            jeu_duo = False




    #début de partie solo
    while jeu_solo:

        if Tour_joueur == 1:
            print("C'est à votre tour de jouer ! \n")
            Tour_joueur = f.suivant(Tour_joueur)
            tir_effectuee = False
            while tir_effectuee is False:
                valid_patern = False
                while valid_patern is False:
                    #propose les actions disponibles au joueur
                    print("Vous avez 5 actions disponible : \n - 1 : afficher vos navires \n - 2 : afficher vos tirs \n - 3 : attaquer l'adversaire \n - 4 : vous passez votre tour\n - 5 : Sauvegarder et quitter la partie\n")
                    action = input("Quelle action voulez vous effectuer  ? (1, 2, 3 ou 4) : ")
                    if re.match(patern_réponse,action):
                        valid_patern = True
                    else:
                        print("Votre réponse n'est pas valide, elle doit être  1, 2, 3 ou 4 . \n ")
                #affiche la grille des bateau du joueur
                if action == '1' :
                    f.affiche_grille(grille_bateau_j1)
                    print("Voici vos navires")
                #affiche la grille des tirs du joueur
                elif action == '2' :
                    f.affiche_grille(grille_attaque_j1)
                    print("Voici vos tirs")
                elif action =='4':
                    print("Vous passez votre Tour\n")
                    tir_effectuee= True
                elif action =='5':
                    print("--------------------------------------")
                    f.save_bateaux_joueur(grille_bateau_j1)
                    f.save_bateaux_IA(grille_bateau_IA)
                    f.save_Tirs_joueur(grille_attaque_j1)
                    f.save_Tirs_IA(tirs_dispo)
                    f.save_cases_occupées_joueur(cases_occupees_j1)
                    f.save_cases_occupées_IA(cases_occupees_IA)
                    exit()
                #fait tirer le joueur et finit son tour
                else :
                    grille_attaque_j1,grille_bateau_IA,cases_occupees_IA = f.attaquer(grille_attaque_j1,grille_bateau_IA,cases_occupees_IA)
                    tir_effectuee = True
                    
        elif Tour_joueur == 2:
            Tour_joueur = f.suivant(Tour_joueur)
            tirs_dispo,grille_bateau_j1,cases_occupees_j1 = f.attaquer_IA(tirs_dispo,grille_bateau_j1,cases_occupees_j1)
        
        #vérifie qu'il reste des bateaux à chaque joueur, si ce n'est pas le cas , finit la partie        
        if len(cases_occupees_IA)==0 :
            print("Le joueur 1 a coulé tous les navires de l'adversaire !!","\n VICTOIRE DU JOUEUR 1 !!!\n")
            print("FIN -----------------------------------------")
            jeu_solo = False

        elif len(cases_occupees_j1)==0:
            print("L'adversaire a coulé tous les navires du joueur 1 !!","\n VICTOIRE DE L'ADVERSAIRE !!!\n")
            print("FIN -----------------------------------------")
            jeu_solo = False    


