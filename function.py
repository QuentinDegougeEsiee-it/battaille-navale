import re

def suivant(joueur):
    """ int -> int
    prend en paramètre l'indice d'un joueur actuel et
    renvoie l'indice du joueur suivant (1 ou 2)
    """
    if joueur == 1:
        return 2
    else:
        return 1
    
def grille_vide():
    """ void -> list
    genere une liste 2D de 10 x 10.
    Les cases vides contiennent (" ").
    """
    tab1= []
    for j in range(10):
        tab2= []
        for i in range(10):
            tab2.append("  ")
        tab1.append(tab2)
    return tab1

grille_bateaux = grille_vide()


def affiche_grille(grille):
    """list -> void
        affiche la grille prise en argument en ajoutant les noms des lignes et colonnes
    """
    
    print("      "+"     ".join(['A','B','C','D','E','F','G','H','I','J'])) 
    #met un espace initial puis affiche les éléments de la liste avec un espace identique entre chaque

    for i in range(1,11):

        print (f"{i:2}",grille[i-1])
        # affiche le numéro de la ligne en utilisant 2 espaces pour l'alignement  puis affiche la ligne de la grille correspondante



def place_bateau(grille_bateaux):
    """ list -> list,list
        demande au joueur de rentrer les position des bateaux sur sa grille de jeu.
        fait les vérication pour empêcher les bateaux d'être positionner en dehors de la grille ou par dessus d'autre bateaux
        renvoie la grille ainsi qu'une liste  comprenant toutes les position occupés par les bateaux
    """
    case_prise=[]
    bateau_dispo= [2]
    pattern = r"^[A-J],(10|[1-9])$"
    while len(bateau_dispo)>0:
        entree_chiffre = False
        #choix du type de bateau
        while entree_chiffre is False:
            print("il reste les bateaux de taille : ", bateau_dispo)
            choix = input("quelle est la taille du bateau que vous souhaitez placer ? : ")
            #vérifie le type de la valeur saisie
            try:
                choix= int(choix)
                entree_chiffre=True
            except:
                print("la valeur saisie n'est pas valide")
        if choix not in bateau_dispo:
            print("votre choix n'est pas dans la liste des bateaux disponibles")
        else:
            #retire le bateau de la taille "choix" de la liste des  bateau disponible
            bateau_dispo.remove(choix)
            pos_valid = False
            while pos_valid is False:
                pos_valid=True
                #demande de rentrer les valeurs des cases
                valid_patern1=False
                while valid_patern1 is False:
                    P1 = input("Veuillez rentrer la première case de votre bateau en majuscule (ex: A,1  ou J,10): ")
                    #vérifie que le format de la saisie correspond bien à [A-J],[1-10]
                    if re.match(pattern, P1):
                        valid_patern1=True
                    else: 
                        print("Erreur dans le format de la saisie, le format doit être comme suit [A-J],[1-10]")
                #convertit la saisie en tuple
                colonne1,ligne1 = P1.split(',')
                colonne1= colonne1.strip()
                ligne1 = int(ligne1.strip())
                tuple1 = (colonne1,ligne1)
                valid_patern2=False
                while valid_patern2 is False:
                    P2 = input("Veuillez rentrer la deuxième case de votre bateau en majuscule(ex: A,2): ")
                    #vérifie que le format de la saisie correspond bien à [A-J],[1-10]
                    if re.match(pattern, P2):
                        valid_patern2=True
                    else: 
                        print("Erreur dans le format de la saisie, le format doit être comme suit [A-J],[1-10]")
                #convertit la saisie en tuple
                colonne2,ligne2 = P2.split(',')
                colonne2= colonne2.strip()
                ligne2 = int(ligne2.strip())
                tuple2 = (colonne2,ligne2)

                #vérifie si la taille du bateau est respecté(1x1)
                if tuple1[0] == tuple2[0] and tuple1[1] == tuple2[1]:
                    print("les position sont invalide, le bateau n'est pas de la bonne taille")
                    pos_valid=False
                #vérifie si le bateau n'est pas en diagonal    
                elif tuple1[0] != tuple2[0] and tuple1[1] != tuple2[1]:
                    print("les position sont invalide, le bateau ne peut pas être de diagonal")
                    pos_valid=False

                elif tuple1[0] == tuple2[0]:
                    #vérifie si la taille du bateau est respecté(ligne)
                    if tuple1[1] - tuple2[1] != choix-1 and tuple2[1] - tuple1[1] != choix-1:
                        print("les position sont invalide, le bateau n'est pas de la bonne taille")
                        pos_valid=False
                    #vérifie si un autre bateau à déja été posé à cette position(ligne)
                    for k in range(choix):
                        case_verif= tuple1[1]-(k-1),ord(tuple1[0])-65
                        if case_verif in case_prise:
                            print("position invalide, les bateau se chevauchent")
                            pos_valid=False
                
                #vérifie si la taille du bateau est respecté(colonne)
                elif tuple1[1] == tuple2[1]:
                    if ord(tuple1[0]) - ord(tuple2[0]) != choix-1 and ord(tuple2[0]) - ord(tuple1[0]) != choix-1:
                        print("les position sont invalide, le bateau n'est pas de la bonne taille")
                        pos_valid=False
                    #vérifie si un autre bateau à déja été posé à cette position(colonne)
                    if ord(tuple1[0]) > ord(tuple2[0]):
                        for k in range(choix):
                            case_verif= tuple1[1]-1,ord(tuple1[0])-65-k
                            if case_verif in case_prise:
                                print("position invalide, les bateau se chevauchent")
                                pos_valid=False
            #fin des vérification, début du remplissage de la matrice bateau
            if tuple1[0] == tuple2[0]:
                if tuple1[1] > tuple2[1]:
                    for j in range(choix):
                        #ajoute le bateau dans la grille
                        grille_bateaux[tuple1[1]-j-1][ord(tuple1[0])-65] = '🚢'
                        #met à jour la liste des cases occupées par un bateau
                        case= tuple1[1]-j-1,ord(tuple1[0])-65
                        case_prise.append(case)
                else:
                    for j in range(choix):
                        grille_bateaux[tuple1[1]+j-1][ord(tuple1[0])-65] = '🚢'
                        case= tuple1[1]+j-1,ord(tuple1[0])-65
                        case_prise.append(case)
            else:
                if tuple1[0] > tuple2[0]:
                    for j in range(choix):
                        grille_bateaux[tuple1[1]-1][ord(tuple1[0])-65-j] = '🚢'
                        case= tuple1[1]-1,ord(tuple1[0])-65-j
                        case_prise.append(case)
                        print("1",case)
                else:
                    for j in range(choix):
                        grille_bateaux[tuple1[1]-1][ord(tuple1[0])-65+j] = '🚢'
                        case= tuple1[1]-1,ord(tuple1[0])-65+j
                        print ("2",case)
                        case_prise.append(case)
            affiche_grille(grille_bateaux)
    print("Tout les bateaux ont été placés")
    return grille_bateaux, case_prise



def attaquer(grille_attaque, grille_bateaux,case_occupee) :
    """ list,list,list -> list, list, list
        Demande la coordonée du tir au joueur, 
        Vérifie que la coordonée est valide et qu'il n'y a pas déjà eu de tir au même emplacement,
        Modifie la grille de tir de joueur attaquant, la liste des bateau restant et  la grille des bateaux du joueur attaqué en conséquence
        et les retourne.
    """
    affiche_grille(grille_attaque)
    pattern = r"^[A-J],(10|[1-9])$"
    tir_effectue= False
    while tir_effectue is False:
        valid_patern1=False
        while valid_patern1 is False:
            pos_tir = input("Veuillez rentrer la case ou vous souhaitez tirer (ex: A,1  ou J,10): ")
            #vérifie que le format de la saisie correspond bien à [A-J],[1-10]
            if re.match(pattern, pos_tir):
                valid_patern1=True
            else: 
                print("Erreur dans le format de la saisie, le format doit être comme suit [A-J],[1-10]")
        #convertit la saisie en tuple
        colonne1,ligne1 = pos_tir.split(',')
        colonne1= colonne1.strip()
        colonne1= int(ord(colonne1)-65)
        ligne1 = int(ligne1.strip())
        ligne1-=1
        tuple1 = (ligne1,colonne1)
        #vérifie que le joueur n'a pas déjà tiré dans cette case
        if grille_attaque[ligne1][colonne1] == '💥' or grille_attaque[ligne1][colonne1] == '🌊' :
            print("Vous avez déjà tiré à cet endroit, merci de choisir d'autre coordonées ! ")
        
        #si le joueur touche : 
        elif grille_bateaux [ligne1][colonne1] == '🚢':
            print("TOUCHÉ !!!")
            grille_attaque[ligne1][colonne1] = '💥'
            grille_bateaux[ligne1][colonne1] = '🔥'
            case_occupee.remove(tuple1)
            tir_effectue=True
        
        #si le joeur rate :
        else :
            print("COULÉ !")
            grille_attaque[ligne1][colonne1] = '🌊'
            tir_effectue=True
    
    return grille_attaque, grille_bateaux, case_occupee
        


                    