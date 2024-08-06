#6) Projete uma função que determine a quantidade de elementos de uma árvore binária.

from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    esq:Arvore
    num:int
    dir:Arvore
Arvore = No | None

def quantos_tem(arvore:Arvore) -> int:
    '''
    >>> t2 = No(None,23,None)
    >>> t3 = No(None,15,None)
    >>> t1 = No(None,13,t3)
    >>> a = No(t1,20,t2)
    >>> quantos_tem(a)
    4
    
    '''

    if arvore is None:
        return 0
    else:
        return 1 + quantos_tem(arvore.esq) + quantos_tem(arvore.dir)

#7) Projete uma função que determine quantos nós em uma árvore binária tem grau 2.

def arvore_grau2(arvore:Arvore) -> int:
    '''
    >>> t2 = No(None,23,None)
    >>> t1 = No(No(None,11,None),13,No(None,14,None))
    >>> a = No(t1,20,t2)
    >>> arvore_grau2(a)
    2
    
    '''
    if arvore is None:
        return 0
    else:
        if arvore.dir is not None and arvore.esq is not None:
            return 1 + arvore_grau2(arvore.esq) + arvore_grau2(arvore.dir)
        else:
            return arvore_grau2(arvore.esq) + arvore_grau2(arvore.dir)

#8) Uma árvore binária cheia é aquela em que todos os seus nós tem grau 0 ou 2. Projete uma função que
#determine se uma árvore binária é cheia.

def arvore_cheia(arvore:Arvore) -> bool:
    '''
Verifica se a arvore está cheia, se estiver cheia retorna True se n retorna false

    >>> t2 = No(None,23,No(None,25,None))
    >>> t1 = No(No(None,11,None),13,No(None,14,None))
    >>> a = No(t1,20,t2)
    >>> arvore_cheia(a)
    False
    
    '''
    
    if arvore is None:
        return False
    else:
        if arvore.dir is None and arvore.esq is None:
            return True   
        elif arvore.dir is not None and arvore.esq is None:
            return False
        elif arvore.esq is not None and arvore.dir is None:
            return False
        else:
            return arvore_cheia(arvore.dir) and arvore_cheia(arvore.esq)
        

# 9) Projete uma função que determine a altura de uma árvore binária.
    
def altura_arvore(arvore:Arvore) -> int:
    '''
    Recebe uma arvore binaria e retorna a altura da arvore.

    >>> t16 = No(None,15,None)
    >>> t15 = No(None,8,t16)
    >>> t14 = No(t15,18,None)
    >>> t13 = No(None,7,t14)
    >>> t12 = No(t13,19,None )
    >>> t11 = No(None,6,t12)
    >>> t10 = No(t11,20,None)
    >>> t9 = No(None,4,None)
    >>> t8 = No(t9,5,t10)
    >>> t4 = No(None,1,None)
    >>> t5 = No(None,3,t8)
    >>> t6 = No(None,35,None)
    >>> t7 = No(None,45,None)
    >>> t2 = No(t4,2,t5)
    >>> t3 = No(t6,39,t7)
    >>> t1 = No(t2,30,t3)
    >>> altura_arvore(t1)
    10
    '''
    if arvore is None:
        return -1
    else:
        if 1 + altura_arvore(arvore.dir) > 1 + altura_arvore(arvore.esq):
            return 1 + altura_arvore(arvore.dir)
        else:
            return 1 + altura_arvore(arvore.esq)
       


#10) Projete uma função que altere os elementos negativos de uma árvore binária para seus valores absolutos.
    
def valor_absolutos(arvore:Arvore):
    if arvore is None:
        return None
    else:
        if arvore.num < 0:
           arvore.num = arvore.num * - 1 
        valor_absolutos(arvore.dir)
        valor_absolutos(arvore.esq)
    
        
#11) Projete uma função que devolva o valor máximo em uma árvore binária ou None se a árvore estiver vazia

def maior_valor(arvore:Arvore) -> int|None:
    '''
    Recebe uma arvore binaria e retorna o maior valor contido nela.

    '''    
    if arvore is None:
        return None
    elif arvore.dir is None and arvore.esq is None:
        return arvore.num
    elif arvore.esq is not None and arvore.dir is None:
        a = maior_valor(arvore.esq)
        assert a is not None
        if a > arvore.num:
            return a
        return arvore.num
    elif arvore.dir is not None and arvore.esq is None:
        a = maior_valor(arvore.dir)
        assert a is not None
        if a > arvore.num:
            return a
        return arvore.num
    else:
        a = maior_valor(arvore.esq)
        b = maior_valor(arvore.dir)
        assert a is not None and b is not None
        if a >= b and a >= arvore.num:
            return a
        elif b > a and b >= arvore.num:
            return b 
        return arvore.num
    
   
#No(esq=No(esq=No(esq=None, num=3, dir=No(esq=None, num=4, dir=None)), num=8, dir=None), num=2, dir=No(esq=No(esq=None, num=7, dir=None), num=3, dir=No(esq=No(esq=None, num=2, dir=None), num=5, dir=None)))

#12)Uma árvore binária balanceada é aquela em que a altura das subárvores a direita e a esquerda diferem
#em no máximo 1 e as duas subárvores também são balanceadas. Projete uma função que verifique se
#uma árvore binária é balanceada.

def balenciada(arvore:Arvore) -> bool:
        
    return arvore is None or (-1 <= altura_arvore(arvore.dir) - altura_arvore(arvore.esq) <=  1 and balenciada(arvore.dir) and balenciada(arvore.esq))
        
           

        



















