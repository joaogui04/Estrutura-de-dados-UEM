#Projete uma função recursiva que conte quantas vezes um número aparece em um arranjo.
from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    primeiro:int
    resto: Lista
Lista = No | None

def Aparece(numero:int, lista:Lista) -> int:
    if lista is None:
        return 0
    else:
        if numero == lista.primeiro:
            return 1 + Aparece(numero, lista.resto)
        else:
            return 0 + Aparece(numero, lista.resto)
            


            