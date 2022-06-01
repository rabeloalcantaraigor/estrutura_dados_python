
import numpy as np

class No:
    
    def __init__(self, valor) -> None:
        self.valor = valor
        self.proximo = None
        
    def mostra_no(self):
        print(self.valor)
        
no1 = No(1)
no1.mostra_no()

no2 = No(2)
no2.mostra_no()

class ListaEncadeada:
    
    def __init__(self) -> None:
        self.primeiro = None