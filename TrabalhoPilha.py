import random

# Nomes: João Guilherme Cabianchi Pires RA: 134747, Leticia Yui Hirata RA: 134737
##################################################### 1 parte do Trabalho  ######################################################################

class Pilha:
    lista: list 
    fim: int   
    tamMax: int  

    def __init__(self,tamanho):
        self.lista = [-1]*tamanho
        self.fim = -1 
        self.tamMax = tamanho


    def Vazia(self):
        if self.fim == -1:
            return True
        else:
            return False
        
    def Cheia(self):
        if self.fim == self.tamMax - 1:
            return True
        else:
            return False

    def Empilha(self,x):
        if self.Cheia():
            print("A Pilha está Cheia")
        else:
            self.fim += 1
            self.lista[self.fim] = x
            
    def Desempilha(self):
        if self.Vazia():
            print("A Pilha está Vazia")
        else:
            x = self.lista[self.fim]
            self.lista[self.fim] = -1
            self.fim -=1
            return x 
    
    def ElementoTopo(self):
        if self.Vazia():
            print("A Pilha está Vazia")
        else:
            return self.lista[self.fim]
    

    def imprime_pilha(self,x):
            if self.lista[x] == -1:
                return ""
            else:
                return self.lista[x]
            
##################################################### 2 parte do Trabalho  ######################################################################

def cria_lista(n):
    n += 2
    y = 0
    lista = []
    while not y == n:
        x ="Lista" + str(y + 1)
        x = Pilha(4)
        lista.append(x)
        y +=1

    return lista


def cria_listaRandom(n):
    lista = []
    while not n == 0:
        lista.append(n)
        lista.append(n)
        lista.append(n)
        lista.append(n)
        n -=1
    return lista

def insere_aleatorio(lista:list,lista_random):
    x = len(lista)
    cont = x-1
    while not cont == 1 : 
        i = 0
        while not i == 4:
            sorteado = random.choice(lista_random)
            lista_random.remove(sorteado)
            lista[cont].Empilha(sorteado)
            i +=1
        
        cont -=1
    return lista
     
def imprime(lista):
    x = len(lista)
    while not x == 0:
        y = lista[x-1]
        print("Lista"+ str(x) +":"+ str(y.imprime_pilha(0)) + " " + str(y.imprime_pilha(1)) + " " + str(y.imprime_pilha(2)) + " " + str(y.imprime_pilha(3)))
        x -=1

def terminou(lista):
    t = True
    x = len(lista) - 1  
    while x >= 0 and t == True:  
        y = lista[x]
        if y.imprime_pilha(0) == y.imprime_pilha(1) == y.imprime_pilha(2) == y.imprime_pilha(3):
            t = True
        else:
            t = False
        x -= 1  
    return t

#Se a pilha de origem estiver vazia, a jogada não é válida.
#Se a pilha de destino estiver cheia (com quatro elementos), a jogada não é válida.
#Se a pilha de origem não estiver vazia mas a pilha de destino estiver, esta é uma troca válida.
#Atenção : se a pilha de origem não estiver vazia e a pilha de destino estiver NEM CHEIA E NEM VAZIA, esta será uma troca válida se o elemento do topo da pilha de origem for igual ao elemento do topo da pilha de destino.

def troca(lista,origem,destino):
    if lista[origem-1].Vazia():
        print("Não pode fazer essa jogada! ")
        print("----Precione Enter para Voltar----")
        input()
    elif lista[destino-1].Cheia():
        print("Não pode fazer essa jogada! ")
        print("----Precione Enter para Voltar----")
        input()
    elif not lista[origem-1].Vazia() and  lista[destino-1].Vazia():
        x = lista[origem-1]
        y = lista[destino-1] 
        w = x.Desempilha()
        y.Empilha(w)
    elif not lista[origem-1].Vazia() and not lista[destino-1].Cheia() and  not lista[destino-1].Vazia() and lista[origem-1].ElementoTopo() == lista[destino-1].ElementoTopo() :
        x = lista[origem-1]
        y = lista[destino-1] 
        w = x.Desempilha()
        y.Empilha(w)

def loopgame(game):
     imprime(game)
     print("Você quer Mover de qual Pilha? OBS:(escrever apenas o numero da lista)")
     x = input()
     print("Para qual pilha? OBS:(escrever apenas o numero da lista) ")
     y = input()
     troca(game,int(x),int(y))

def main():
        final = False
        print("Esse é o jogo da Pilha!")
        n = input("Com quantas listas você vai quer Jogar?(1 - 7):")
        n = int(n)
        if n > 7 or n < 1:
            main()
        lista = cria_lista(n)
        lista_random = cria_listaRandom(n)
        game = insere_aleatorio(lista,lista_random)
        while final == False:
            loopgame(game)
            final = terminou(game)
        
        print("Você Terminou o GAME!!!")
        
     
main()