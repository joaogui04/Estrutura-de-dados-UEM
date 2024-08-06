#Projete uma função recursiva que determine se um valor está em um arranjo ordenado. Implemente a
#função usando busca binária.
from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    esq: Lista
    num:int
    dir: Lista
Lista = No | None

def buscabinaria(lista:Lista, numero:int):
    if lista is None:
        return False
    else:
        if numero == lista.num:
            return True
        elif numero < lista.num:
            return buscabinaria(lista.esq, numero)
        elif numero > lista.num:
            return buscabinaria(lista.dir, numero)

