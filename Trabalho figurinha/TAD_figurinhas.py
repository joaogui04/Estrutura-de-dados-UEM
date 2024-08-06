from __future__ import annotations
from ed import array

            
class Album_figurinha:
    '''
     Um album de figurinha
    '''
    
  
    def __init__(self):
        '''

        Cria um Album de figurinhas de tamanho escolhido por *tamanho*

        Exemplo
        >>> b = Album_figurinha()
        >>> b.str_figurinhas()
        '[]'

        '''
        
    def insere(self,figurinha:int):
        '''

        Se a figurinha não for repetida adiciona no Album de figurinha,
        Se for repetida adiciona 1 na quantidade de figurinhas repetidas. 

        Exemplo
        >>> b = Album_figurinha(31)
        >>> b.insere(8)
        >>> b.str_figurinhas()
        '[8]'
        >>> b.insere(1)
        >>> b.str_figurinhas()
        '[1, 8]'
        >>> b.insere(5)
        >>> b.str_figurinhas()
        '[1, 5, 8]'
        >>> b.insere(30)
        >>> b.str_figurinhas()
        '[1, 5, 8, 30]'

        #>>> b.insere(31)
        
        Self. 
        '''
     
       
        

    def remove(self,figurinha:int):
        '''

        Se a figurinha não for repetida, remove a figurinha do album de figurinha 
        se for repetida, diminui 1 na quantidade de figurinhas repetidas.


        Exemplo
        >>> b = Album_figurinha(30)
        >>> b.insere(5)
        >>> b.insere(1)
        >>> b.insere(20)
        >>> b.str_figurinhas()
        '[1, 5, 20]'
        >>> b.remove(1)
        >>> b.str_figurinhas()
        '[5, 20]'
        >>> b.remove(20)
        >>> b.str_figurinhas()
        '[5]'
        >>> b.remove(5)
        >>> b.str_figurinhas()
        '[]'
        >>> b.insere(9)

        #>>> b.remove(3)
        Traceback (most recent call last):
            ...
        ValueError: Essa figurinha não está no Album_figurinha
        >>> b.remove(9)

        #>>> b.remove(1)
        Traceback (most recent call last):
            ...
        ValueError: Essa figurinha não está no Album_figurinha
        >>> b.str_repetidas()
        '[]'
        >>> b.insere(9)
        >>> b.insere(9)
        >>> b.insere(9)
        >>> b.str_repetidas()
        '[9 (2)]'
        >>> b.remove(9)
        >>> b.str_repetidas()
        '[9 (1)]'
        >>> b.remove(9)
        >>> b.str_repetidas()
        '[]'
        '''
       

    def str_figurinhas(self):
        '''
        Mostra quais figurinhas você tem dentro do Album de figurinhas no formato de uma str . 

        Exemplo
        >>> b = Album_figurinha(10)
        >>> b.str_figurinhas()
        '[]'
        >>> b.insere(2)
        >>> b.str_figurinhas()
        '[2]'
        >>> b.remove(2)
        >>> b.str_figurinhas()
        '[]'

        '''
        
        

    def str_repetidas(self):
        '''
        Mostra quais as figurinhas que você tem repeditas e qual a quantidade delas no fomato de uma str.

        Exemplo  
        >>> b = Album_figurinha(10)
        >>> b.insere(2)
        >>> b.insere(2)
        >>> b.str_repetidas()
        '[2 (1)]'
        >>> b.insere(1)
        >>> b.str_repetidas()
        '[2 (1)]'
        >>> b.insere(1)
        >>> b.str_repetidas()
        '[1 (1), 2 (1)]'
        >>> b.remove(2)
        >>> b.str_repetidas()
        '[1 (1)]'
        '''
        


    def trocar(self, colecao:array):
        '''
        Realizar a troca máxima de figurinhas entre duas coleções

        >>> b = Album_figurinha(15)
        >>> a = Album_figurinha(15)
        >>> b.insere(1)
        >>> b.insere(2)
        >>> b.insere(3)
        >>> b.insere(4)
        >>> b.insere(5)
        >>> b.insere(1)
        >>> b.insere(2)
        >>> b.insere(3)
        >>> b.insere(4)
        >>> b.insere(5)
        >>> b.str_repetidas()
        '[1 (1), 2 (1), 3 (1), 4 (1), 5 (1)]'
        >>> a.insere(6)
        >>> a.insere(7)
        >>> a.insere(8)
        >>> a.insere(9)
        >>> a.insere(6)
        >>> a.insere(7)
        >>> a.insere(8)
        >>> a.insere(9)
        >>> a.insere(10)
        >>> a.insere(10)
        >>> a.str_repetidas()
        '[6 (1), 7 (1), 8 (1), 9 (1), 10 (1)]'
        >>> b.trocar(a)
        >>> b.str_repetidas()
        '[]'
        >>> a.str_repetidas()
        '[]'
        >>> b.str_figurinhas()
        '[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]'
        >>> a.str_figurinhas()
        '[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]'

        >>> b = Album_figurinha(10)
        >>> a = Album_figurinha(9)
        >>> a.trocar(b)
        Traceback (most recent call last):
            ...
        ValueError: Não é possivel fazer a troca pois os albuns são diferentes

        >>> b = Album_figurinha(10) 
        >>> a = Album_figurinha(10)
        >>> b.insere(1)
        >>> b.insere(2)
        >>> b.insere(3)
        >>> b.insere(1)
        >>> a.insere(2)
        >>> a.insere(3)
        >>> a.insere(4)
        >>> a.insere(4)
        >>> a.insere(5)
        >>> a.insere(5)
        >>> a.str_repetidas()
        '[4 (1), 5 (1)]'
        >>> b.str_repetidas()
        '[1 (1)]'
        >>> b.trocar(a)
        >>> a.str_repetidas()
        '[5 (1)]'
        >>> b.str_repetidas()
        '[]'
        >>> b.str_figurinhas()
        '[1, 2, 3, 4]'
        >>> a.str_figurinhas()
        '[1, 2, 3, 4, 5]'

        '''
    