from ed import array

def buscabinaria(lista:array[int], chave: int):
    '''
    >>> buscabinaria([1,4,5,7,8,9], 4)
    1
    >>> buscabinaria([3, 6, 8, 9, 20, 21, 22, 23, 30, 40, 45, 46, 50, 60], 6)
    1
    >>> buscabinaria([3, 6, 8, 9, 20, 21, 22, 23, 30, 40, 45, 46, 50, 60], 30)
    8
    >>> buscabinaria([3, 6, 8, 9, 20, 21, 22, 23, 30, 40, 45, 46, 50, 60], 41)
    Traceback (most recent call last):
            ...
    ValueError: essa chave n tem na lista
    >>> buscabinaria([3, 6, 8, 9, 20, 21, 22, 23, 30, 40, 45, 46, 50, 60], 70)
    Traceback (most recent call last):
            ...
    ValueError: essa chave n tem na lista

    '''
    inicio = 0
    fim = len(lista) - 1
    meio = ((inicio + fim) // 2)
    while chave != lista[meio] and fim > inicio:
        if chave < lista[meio]:
            fim = meio - 1
            meio = ((inicio + fim) // 2)
        else:
            inicio = meio + 1
            meio = ((inicio + fim) // 2)
    
    if chave == lista[meio]:
        return meio
    else: 
        raise ValueError('essa chave n tem na lista')
    


            