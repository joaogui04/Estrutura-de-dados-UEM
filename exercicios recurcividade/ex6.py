#Projete uma função recursiva que receba como entrada uma string e um número natural n e devolva
#a string repetida n vezes. Por exemplo, para a string 'casa' e n = 3, a função deve produzir
#'casacasacasa'. Não use o operador de repetição de string (*)!

def repetida(paravra:str,numero:int) -> str:
    if numero == 1:
        return paravra
    else:
        return paravra + repetida(paravra,numero - 1) 