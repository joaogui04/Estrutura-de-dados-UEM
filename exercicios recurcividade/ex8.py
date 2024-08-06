#Projete uma função recursiva que receba como entrada um número a (diferente de 0) e um número
#natural n e calcule o valor a elevado a n
def calcula_elevado(numero:int, elevado:int) -> int:
    if elevado == 1:
        return numero
    else:
        return numero * calcula_elevado(numero, elevado - 1)
