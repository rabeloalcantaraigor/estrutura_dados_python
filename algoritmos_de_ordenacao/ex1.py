
# Exercício comparativo vetor ordenado e ordenação

import numpy as np

import random

class VetorOrdenado:
    
    def __init__(self, capacidade) -> None:
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=float)
        
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade atingida.')
            return
        
        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultima_posicao:
                posicao = i + 1
        
        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1
        
        self.valores[posicao] = valor
        self.ultima_posicao += 1
        
def insere_ordenado(valores):
    vetor = VetorOrdenado(len(valores))
    for i in range(len(valores)):
        vetor.insere(i)
            
vetor = []

for _ in range(5000):
    vetor.append(round(random.random(), 4))
    
print(type(vetor))

vetor = np.array(vetor)
print(type(vetor))
vetor[:5]
print(len(vetor))


print(insere_ordenado(vetor.copy()))