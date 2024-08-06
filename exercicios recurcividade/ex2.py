# Projete uma função recursiva que receba como entrada uma lista encadeada e crie uma nova lista
#encadeada com os elementos positivos da lista de entrada
from __future__ import annotations
from dataclasses import dataclass

@dataclass 
class No:
    primeiro:int
    Resto:Lista
Lista = No | None



def crialista(lista:Lista) -> Lista:
    '''
    >>> a = No(7,No(2,No(-1, None)))
    >>> crialista(a)
    No(primeiro=7, Resto=No(primeiro=2, Resto=None))
    
    '''
    if lista is None:
        return None
    else:
        if lista.primeiro > 0:
            return No(lista.primeiro, crialista(lista.Resto))
        else:
            return crialista(lista.Resto)
            





























