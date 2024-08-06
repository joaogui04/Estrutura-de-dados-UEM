#Projete uma função recursiva que encontre o valor máximo de uma lista encadeada. Se a lista for
#vazia, a função deve devolver None

from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    primeiro:int
    resto: Lista
Lista = No | None

def valormaximo(lista:Lista) -> int | None: 
    if lista is None:
        return None
    else:
        if valormaximo(lista.resto) is None or lista.primeiro > valormaximo(lista.resto): # type: ignore
            return lista.primeiro
        else:
            return valormaximo(lista.resto)
        

