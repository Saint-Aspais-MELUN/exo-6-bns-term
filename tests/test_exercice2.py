from exercices.exercice2 import *
F = File()

def test_F_est_vide():
    assert F.est_vide() == True
    
F.enfile(2)
F.affiche()

def test_ F_est_vide():
    assert  F.est_vide() == False
    
F.enfile(5)
F.enfile(7)
F.affiche()

def test_F_defile():
    assert F.defile() == 2
    assert F.defile() == 5
    
def test_F_affiche():
     assert F.affiche() == 7
    
    
