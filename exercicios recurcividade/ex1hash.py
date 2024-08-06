from __future__ import annotations
from dataclasses import dataclass 


def dpy(tamanho:int,elemento:int):
    A = 1.618033
    resultado = tamanho * (elemento * A % 1)
    return resultado


@dataclass
class Chave:
    chave:str
    valor:int
    

class hsash:
    ok: bool
    tabela: list
    num_itens: int
    tamanho_da_tabela:int
   
    def __init__(self, tamanho_tabela:int) -> None:

        self.ok = False
        self.tamanho_da_tabela = tamanho_tabela
        self.num_itens = 0
        self.tabela = [[]for _ in range(self.tamanho_da_tabela)]


    def get(self, chave: str) -> int | None:
    # procurar por chave em self.tabela[h(chave)]
        x = hash(chave) % self.tamanho_da_tabela
        for elemento in self.tabela[x]:
            if elemento.chave == chave:
                return elemento.valor
        return None
       
    def numero_itens(self) -> int:
        return self.num_itens
       

    def associa(self, chave: str, valor: int):
    # inserir (chave, valor) em self.tabela[h(chave)]
    # ou atualizar o valor associado com a chave  
        x = hash(chave) % self.tamanho_da_tabela
        for elemento in self.tabela[x]:
            if elemento.chave == chave:
                elemento.valor = valor
                return 
        novo = Chave(chave,valor)
        self.tabela[x].append(novo)
        self.num_itens += 1
        print(self.tabela)
        if self.num_itens > self.tamanho_da_tabela * 10:
            self.ok = True
            print('ok')
            tam = self.tamanho_da_tabela
            self.tamanho_da_tabela = self.tamanho_da_tabela * 2
            a = hsash(self.tamanho_da_tabela)
            for x in range(tam):
                for y in self.tabela[x]:
                    a.associa(y.chave, y.valor)

            self.tabela = a.tabela
        


    
    def remove(self, chave: str):
        x = hash(chave) % self.tamanho_da_tabela
        for elemento in self.tabela[x]:
            if elemento.chave == chave:
                self.tabela[x].remove(elemento)
                self.num_itens -= 1
        print(self.tabela)

        if self.ok is True and (self.tamanho_da_tabela * 10)/ 2 > self.num_itens * self.tamanho_da_tabela:
            print('ok')
            tam = self.tamanho_da_tabela
            self.tamanho_da_tabela = int(self.tamanho_da_tabela / 2)
            a = hsash(self.tamanho_da_tabela)
            for x in range(tam):
                for y in self.tabela[x]:
                    a.associa(y.chave, y.valor)
            self.tabela = a.tabela
            print(self.tabela)
            






 # se o tamanho numero de itens for 10 vezes maior q o tamanho da tabela vc dobra o tamanho da tabela e 
 #Primeiro vc vai receber uma chave e um valor dps vai pegar essa chave e pegar a hash dela dps vai fazer mod do tamanho da lista em cima dessa hash e vc vai ter o indice então é vc adiconar o valor nessa hash 