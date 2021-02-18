from exercices.exercice2 import *
F = File()

def test_F.est_vide():
    assert F.est_vide() == True
    
F.enfile(2)
F.affiche()

def test_ F.est_vide():
    assert  F.est_vide() == False
    
F.enfile(5)
F.enfile(7)
F.affiche()

def test_F.defile():
    assert F.defile() == 2
    assert F.defile() == 5
    
def test_F.affiche():
     assert F.affiche() == 7
    
    
"""" 
Voilà ce qui est dans le pdf
>>> F = File()
>>> F.est_vide()
True
>>> F.enfile(2)
>>> F.affiche()
2
>>> F.est_vide()
False
>>> F.enfile(5)
>>> F.enfile(7)
>>> F.affiche()
7
5
2
>>> F.defile()
2
>>> F.defile()
5
>>> F.affiche()
7
"""

    
