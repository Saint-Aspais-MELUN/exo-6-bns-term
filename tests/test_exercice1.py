from exercices.exercice1 import *

def test_taille():
    ## Ici le code d'initialisation si nécessaire
    a = {
        'F':['B','G'],
        'B':['A','D'],
        'A':['',''],
        'D':['C','E'],
        'C':['',''],
        'E':['',''],
        'G':['','I'],
        'I':['','H'],
        'H':['','']
    }
    assert taille(a,'F') == 9