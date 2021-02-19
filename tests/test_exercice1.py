from exercices.exercice1 import *

def test_rendu():
    
    assert rendu(13) == [2,1,1]
    assert rendu(64) == [12,2,0]
    assert rendu(89) == [17,2,0]
