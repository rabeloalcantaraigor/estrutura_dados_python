
import numpy as np

class No:
    
    def __init__(self, valor) -> None:
        self.valor = valor
        self.proximo = None
        
    def mostrar_no(self):
        print(self.valor)
        
no1 = No(1)
no1.mostrar_no()

no2 = No(2)
no2.mostrar_no()

class ListaEncadeada:
    
    def __init__(self) -> None:
        self.primeiro = None
        
    def insere_inicio(self, valor):
        novo = No(valor)
        novo.proximo = self.primeiro
        self.primeiro = novo
        
    def mostrar(self):
        atual = self.primeiro
        while atual != None:
            atual.mostrar_no()
            atual = atual.proximo
            
lista = ListaEncadeada()

lista.insere_inicio(1)

print(lista.primeiro)

lista.mostrar()

lista.insere_inicio(2)
lista.mostrar()

print(lista.primeiro)

lista.primeiro.mostrar_no()

print(lista.primeiro.proximo)

lista.insere_inicio(3)
lista.insere_inicio(4)
lista.insere_inicio(4)
lista.mostrar()

print(lista.primeiro.proximo.proximo.proximo.proximo)