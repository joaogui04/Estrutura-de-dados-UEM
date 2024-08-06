#Projete uma função recursiva que encontre o tamanho máximo entre todas as strings de um arranjo
#de strings.
from __future__ import annotations
from dataclasses import dataclass
@dataclass
class No:
    primeiro: str
    resto: Lista
Lista = No | None

def tamanho_maximostr(palavra:Lista) -> int:
    if palavra is None:
        return 0
    else:
        if len(palavra.primeiro) > tamanho_maximostr(palavra.resto):
            return len(palavra.primeiro)
        else:
            return tamanho_maximostr(palavra.resto)