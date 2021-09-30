"""
Visualisation du jeu/probleme de la Tours de Hanoi, resolution par recursivite.

Possibilite de choisir les tailles des disques dans l'interface, remplir avec des espaces, odre pas important.


"""

#Modules import
from hanoi_vision import Visualisation_hanoi
import tkinter as tk

#Variables
v = Visualisation_hanoi([[5,4,3,2,1],[],[]])
hanoi = [[5,4,3,2,1],[],[]]

#Fonctions
def bouge(hanoi, v, x, y):
    """
    Fonction bouge elemnt de tour x a tour y en verifiant que cella est possible.

    Args:
        hanoi (liste de liste (matrice)): les  3 tours
        v (Objet, Visualisation_hanoi): Visualisation tkinter
        x (int): tour de depart
        y (int): tour d'arivee

    Returns:
        list: matrice avec permutations implementees. 
    """
    if len(hanoi[x])>0 and (hanoi[y] == [] or hanoi[x][-1] < hanoi[y][-1] ):
        hanoi[y].append(hanoi[x].pop(-1))

    else:
        print("Mouvement interdit.")
    v.mise_a_jour(hanoi)
    return hanoi



def deplace2disques(hanoi, v, depart, arrivee, intermediaire):
    """deplace 2 disques d'une tours a l'autre

    Args:
        hanoi (liste de liste (matrice)): les  3 tours
        v (Objet, Visualisation_hanoi): Visualisation tkinter
        depart (int): tour de depart
        arrivee (int): tour d'arivee
        intermediaire (int): tour intermediaire pour le mouvement

    Returns:
        matrice (liste de liste): matrice avec permutations implementees. 
    """
    hanoi = bouge(hanoi, v, depart, intermediaire)
    hanoi = bouge(hanoi, v, depart, arrivee)
    hanoi = bouge(hanoi, v, intermediaire, arrivee)
    return hanoi



def deplace_disques(n, hanoi, v, depart, arrivee, inter):
    """Fonction qui resoud la tour hanoi en utilisant la recursivite

    Args:
        n (int): nombre de disques dans pile de depart
        hanoi (liste de liste (matrice)): les  3 tours
        v (Objet, Visualisation_hanoi): Visualisation tkinter
        depart (int): tour de depart
        arrivee (int): tour d'arivee
        intermediaire (int): tour intermediaire pour le mouvement

    Return:
        rien
    """
    if n == 2:
        deplace2disques(hanoi, v, depart, arrivee, inter)
        return
    else:
        deplace_disques(n-1, hanoi, v, depart, inter, arrivee)
        bouge(hanoi, v, depart, arrivee)
        deplace_disques(n-1, hanoi, v, inter, arrivee, depart)




#Tests
def test1():
    hanoi = [[5,4,3,2,1],[],[]]
    for x in range(5):
        hanoi = bouge(hanoi, v, 0, 1)

def test2():
    hanoi = [[5,4,3,2,1],[],[]]
    deplace2disques(hanoi, v, 0, 2, 1)
    bouge(hanoi, v, 0, 1)
    deplace2disques(hanoi, v, 2, 0, 1)
    bouge(hanoi, v, 1, 2)
    deplace2disques(hanoi, v, 0, 2, 1)

def test3():
    deplace_disques(len(set_matrix()[0]),set_matrix(), v,0,2,1)
    



#Fonctions Tkinter
def start():
    """
    Cree nouvelle matrice et commence le programme
    """
    set_matrix()
    test3()

def restart():
    """
    Remet les disques dans la premiere tour
    """
    v.mise_a_jour(set_matrix())

def set_matrix():
    """
    Prend les chiffres dans l'input et les transformes en matrice jouable

    Returns:
        [matrice, liste de liste]: matrices des trois tours
    """
    matrix = entry.get()
    format_matrix = matrix.split()
    if format_matrix == []:
        return [[5,4,3,2,1],[],[]]
    format_matrix = [int(x) for x in format_matrix]
    format_matrix.sort(reverse=True)
    hanoi = [[x for x in format_matrix],[],[]]
    return hanoi


#UI Tkinter

start_button = tk.Button(v.visu, text = "Start", command = start, bg="red", height=4, width=9)
start_button.place(x=700, y= 650)

restart_button = tk.Button(v.visu, text = "Restart", command = restart, bg="purple", height=4, width=9)
restart_button.place(x=10, y= 650)

entry_default = tk.StringVar(v.visu, value="5 4 3 2 1")
entry = tk.Entry(v.visu, bd = 5, textvariable=entry_default)
entry.pack()

v.visu.resizable(False, False)

v.visu.mainloop()