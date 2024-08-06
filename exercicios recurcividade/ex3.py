#Projete uma função recursiva que receba como entrada uma lista encadeada de strings e um número
#natural n, e modifique as strings da lista para que todas fiquem com tamanho n. Se um string tem
#tamanho maior que n, os caracteres do final devem ser descartados. Se uma string tem tamanho menor
#que n, espaços em branco devem ser adicionados ao final da string.

from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    Primeiro:str
    Resto:Lista
Lista = No | None

def mudatamanho(lista:Lista, tamanho:int) -> Lista:
    '''
    >>> a = No('joao',No('oi',No('pica', None)))
    >>> mudatamanho(a, 4)
    No(Primeiro='joao', Resto=No(Primeiro='oi  ', Resto=No(Primeiro='pica', Resto=None)))
    
    '''
    if lista is None:
       return None
    else:
        t = tamanho - len(lista.Primeiro)
        if len(lista.Primeiro) > tamanho:
            return  No(lista.Primeiro[:tamanho], mudatamanho(lista.Resto, tamanho))
        else:
            return No(lista.Primeiro + ' ' * t, mudatamanho(lista.Resto, tamanho))
