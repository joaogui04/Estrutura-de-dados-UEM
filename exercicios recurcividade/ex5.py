#Projete uma função recursiva que receba como entrada um número natural n e calcule o produto dos
#números 1, 2, · · · , n.

def produto(numero:int) -> int:
    if numero == 1:
        return numero
    else:
        return numero * produto(numero - 1)