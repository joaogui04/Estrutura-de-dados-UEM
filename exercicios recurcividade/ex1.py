from __future__ import annotations
from dataclasses import dataclass


@dataclass

class No:
    primeiro: int
    resto: Lista 
Lista = No | None

def verifica_impar(ista:Lista) -> bool:
    '''
    >>> a = No(7,No(2,No(1, None)))
    >>> 
    '''
    if ista is None:
        return False
    else:
        return ista.primeiro % 2 != 0 or verifica_impar(ista.resto)
        

            
        
   