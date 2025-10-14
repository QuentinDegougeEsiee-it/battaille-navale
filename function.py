def suivant(joueur):
    """ int -> int
    prend en paramètre l'indice d'un joueur actuel et
    renvoie l'indice du joueur suivant (0 ou 1)
    """
    if joueur == 1:
        return 0
    else:
        return 1
    
def grille_vide():
    """ void -> list
    genere une liste 2D de 10 x 10.
    Les cases vides contiennent (" ").
    """
    tab1= []
    tab2= []
    for j in range(10):
        tab2.append(" ")
    for i in range(10):
        tab1.append(tab2)
    return tab1

def affiche_grille(grille):
    """list -> void
        affiche la grille prise en argument en ajoutant les noms des lignes et colonnes
    """
    
    print("     "+"    ".join(['A','B','C','D','E','F','G','H','I','J'])) 
    #met un espace initial puis affiche les éléments de la liste avec un espace identique entre chaque

    for i in range(10):

        print (f"{i+1:2}",grille[i])
        # affiche le numéro de la ligne en utilisant 2 espaces pour l'alignement  puis affiche la ligne de la grille correspondante