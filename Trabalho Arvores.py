
from __future__ import annotations
from dataclasses import dataclass


@dataclass
class No:
    esq:Arvore
    num:int
    dir:Arvore
Arvore = No|None


#1)

def criar_arvoreABB(lista:list[int]) -> Arvore:
    '''
    Recebe uma lista ordenada de inteiros e retorna uma Árvore de Busca Binária. 

    >>> criar_arvoreABB([3, 6, 8, 9, 20, 21, 22, 23, 30, 40, 45, 46, 50, 60])
    No(esq=No(esq=No(esq=No(esq=None, num=3, dir=None), num=6, dir=No(esq=None, num=8, dir=None)), num=9, dir=No(esq=No(esq=None, num=20, dir=None), num=21, dir=No(esq=None, num=22, dir=None))), num=23, dir=No(esq=No(esq=No(esq=None, num=30, dir=None), num=40, dir=No(esq=None, num=45, dir=None)), num=46, dir=No(esq=No(esq=None, num=50, dir=None), num=60, dir=None)))
    
    
    >>> criar_arvoreABB([1,2,4,5])
    No(esq=No(esq=No(esq=None, num=1, dir=None), num=2, dir=None), num=4, dir=No(esq=None, num=5, dir=None))
         4
       /   \
     2      5
    /
   1

    >>> criar_arvoreABB([])

    '''
    if lista == []:
        return None
    return No(criar_arvoreABB(lista[:len(lista)// 2]), lista[len(lista)// 2], criar_arvoreABB(lista[len(lista)// 2 + 1:]))



#2)

def elementos_iguais(arvore1:Arvore, arvore2:Arvore) -> bool:
    '''
    Recebe duas Árvore de Busca Binária se elas forem iguais retorna True, caso ao contrário retorna False.

    >>> b = No(No(None, 1, None), 2, No(No(None, 4, None), 5, No(None, 7, None)))

        5
      /   \
     2     7
   /  \    
  1    4  

    >>> a = No(No(None, 1, None), 2, No(None, 5, None))

        2
      /   \
     1     5



    >>> elementos_iguais(a,b)
    False
    >>> b = No(No(None, 1, None), 2, No(No(None, 4, None), 5, No(None, 7, None)))

        5
      /   \
     2     7
   /  \    
  1    4

    >>> a = No(No(None, 1, None), 2, No(No(None, 4, None), 5, No(None, 7, None)))

        5
      /   \
     2     7
   /  \    
  1    4

    >>> elementos_iguais(a,b)
    True
    >>> a = None
    >>> b = None
    >>> elementos_iguais(a,b)
    True
    
    '''
    if arvore2 is None:
        return True
    else:
        return buscabinaria_arvore(arvore1, arvore2.num) and elementos_iguais(arvore1,arvore2.dir) and elementos_iguais(arvore1,arvore2.esq)
        

def buscabinaria_arvore(arvore:Arvore, chave:int) -> bool:
    if arvore is None:
        return False
    else:
        if chave == arvore.num:
            return True
        elif chave > arvore.num:
            return buscabinaria_arvore(arvore.dir,chave)
        else:
            return buscabinaria_arvore(arvore.esq,chave)
            
            

#3) 

def caminho_maximo(arvore:Arvore) -> list:
    '''
    Recebe uma Árvore Binária e retona uma lista com os maiores caminhos da arvore.

    >>> t2 = No(No(None,7,None),10,No(None,15,None))
    >>> t3 = No(No(None,30,None),40,No(None,45,None)) 
    >>> t1 =No(t2,20,t3)
    
        20
      /    \
    10      40
   /  \    /  \
  7   15  30  45
  

    >>> caminho_maximo(t1)
    [[20, 10, 7], [20, 10, 15], [20, 40, 30], [20, 40, 45]]

    >>> t3 = No(None,40,No(None,45,None))
    >>> t1 =No(None,20,t3)

        20
           \
            40
              \
               45


    >>> caminho_maximo(t1)
    [[20, 40, 45]]

    >>> a = No(No(None, 1, None), 2, No(None, 5, None))

        2
      /   \
     1     5
   
    
    >>> caminho_maximo(a)
    [[2, 1], [2, 5]]
    

    >>> b = None 
    >>> caminho_maximo(b)
    []

    '''
    if arvore is None:
        return []
    altura1 = altura_arvore(arvore.esq)
    altura2 = altura_arvore(arvore.dir)
    if altura1 > altura2:
        caminho = caminho_maximo(arvore.esq)
    elif altura1 < altura2:
        caminho = caminho_maximo(arvore.dir)
    else: 
        if altura1 == -1 and altura2 == -1:
            return [[arvore.num]]
        caminho = caminho_maximo(arvore.esq) + caminho_maximo(arvore.dir)
    tam_caminho = len(caminho)
    for x in range(tam_caminho):
        caminho[x] = [arvore.num] + caminho[x]
    return caminho

def altura_arvore(arvore:Arvore) -> int:
    
    if arvore is None:
        return -1
    else:
        if 1 + altura_arvore(arvore.dir) > 1 + altura_arvore(arvore.esq):
            return 1 + altura_arvore(arvore.dir)
        else:
            return 1 + altura_arvore(arvore.esq)
        


      