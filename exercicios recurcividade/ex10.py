#Projete uma função recursiva que concatene todos as strings de um arranjo de strings
from __future__ import annotations
from dataclasses import dataclass
@dataclass
class No:
    primeiro:str
    resto: Lista
Lista = No | None

def concatena(palavras:Lista) -> str:
    if palavras is None:
        return ''
    else:
        return palavras.primeiro + concatena(palavras.resto)