import numpy as np
import random
import timeit

class VetorOrdenado:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=float)
    
    # O(n)
    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio.')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i])

    #O(n)
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida.')
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
    
    # O(n)
    def pesquisa_linear(self, valor):
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] > valor:
                return -1
            if self.valores[i] == valor:
                return i
            if i == self.ultima_posicao:
                return -1
    
    # O(log n)
    def pesquisa_binaria(self, valor):
        limite_inferior = 0
        limite_superior = self.ultima_posicao
        
        while True:
            posicao_atual = int((limite_inferior + limite_superior) / 2)
            # Se achou na primeira tentativa
            if self.valores[posicao_atual] == valor:
                return posicao_atual
            # Se não achou
            elif limite_inferior > limite_superior:
                return -1
            # Divide os limites
            else:
                # Limite inferior
                if self.valores[posicao_atual] < valor:
                    limite_inferior = posicao_atual + 1
                # Limite superior
                else:
                    limite_superior = posicao_atual - 1
                  
    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == 1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
                
            self.ultima_posicao -= 1
            
class VetorNaoOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=float)
    
    #O(n)
    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i])
                
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capcidade máxima atingida.')
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor
            
    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
                return i
        return -1
    
    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            
            self.ultima_posicao -= 1

round(random.random(), 4)
elementos = []
for _ in range(10000):
    elementos.append(round(random.random(), 4))            

print(len(elementos))
print(elementos[0:10])

def insere_nao_ordenado(lista):
    vetor = VetorNaoOrdenado(len(lista))
    for i in lista:
        vetor.insere(i)
    return vetor

def insere_ordenado(lista):
    vetor = VetorOrdenado(len(lista))
    for i in lista:
        vetor.insere(i)
    return vetor

vetor_nao_ordenado = insere_nao_ordenado(elementos)
len(vetor_nao_ordenado.valores)

vetor_ordenado = insere_ordenado(elementos)
len(vetor_nao_ordenado.valores)

pesquisa = []
for _ in range(10000):
    pesquisa.append(round(random.random(), 4))
len(pesquisa)

def pesquisa_nao_ordenado(lista):
    for i in lista:
        vetor_nao_ordenado.pesquisa(i)


vetor = VetorOrdenado(10)
vetor.insere(8)
vetor.insere(9)
vetor.insere(4)
vetor.insere(1)
vetor.insere(5)
vetor.insere(7)
vetor.insere(11)
vetor.insere(13)
vetor.insere(2)
vetor.imprime()

#print(vetor.pesquisa_binaria(20))
# print(vetor.pesquisar_binaria(2))
# print(vetor.pesquisar_binaria(9))

# vetor.excluir(5)
# vetor.excluir(1)
# vetor.excluir(8)
# vetor.excluir(9)
# vetor.imprime()

# print(vetor.pesquisar(9))




