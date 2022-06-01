import numpy as np

class VetorNaoOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)
    
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
                
vetor = VetorNaoOrdenado(5)    

vetor.imprime()

vetor.insere(3)
vetor.insere(5)
vetor.insere(8)
vetor.insere(1)

vetor.imprime()

vetor.insere(7)

vetor.imprime()

print(vetor.pesquisar(8))

print(vetor.pesquisar(9))

print(vetor.pesquisar(3))

print(vetor.ultima_posicao)

vetor.excluir(5)

vetor.imprime()

vetor.excluir(3)

vetor.imprime()

vetor.excluir(7)

vetor.imprime()


vetor.insere(5)
vetor.insere(9)
vetor.imprime()