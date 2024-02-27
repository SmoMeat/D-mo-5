# La fonction ci-dessous est une fonction de test pour la fonction myst. À l’aide de cette fonction,
# déduisez la spécification de la fonction myst et écrivez une définition de cette fonction.

def testMyst():
    assert myst(11,42,13) == 42
    assert myst(-6,-5,13) == 13
    assert myst(-6,-5, 3) == -6
    assert myst(-6,-5, 6) == 6

def myst(*args):
    max = args[0]
    for arg in args:
        if abs(arg) > abs(max):
            max = arg
        elif abs(arg) == abs(max) and arg > max:
            max = arg
    return max

testMyst()