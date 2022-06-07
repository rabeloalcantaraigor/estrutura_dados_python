
# Árvore binária de busca

class No:
    def __init__(self, valor) -> None:
        self.valor = valor
        self.esquerda = None
        self.direita = None
        
    def mostra_no(self):
        print(self.valor)
        
class ArvoreBinariaBusca:
    def __init__(self) -> None:
        self.raiz = None
        self.ligacoes = []
    
    def inserir(self, valor):
        novo = No(valor)
        # Se a árvore estiver vazia
        if self.raiz == None:
            self.raiz= novo
        else:
            atual = self.raiz
            while True:
                pai = atual
                # Esquerda
                if valor < atual.valor:
                    atual = atual.esquerda
                    if atual == None:
                        pai.esquerda = novo
                        self.ligacoes.append(str(pai.valor) + '->' + str(novo.valor))
                        return
                # Direita
                else:
                    atual = atual.direita
                    if atual == None:
                        pai.direita = novo
                        self.ligacoes.append(str(pai.valor) + '->' + str(novo.valor))
                        return
                    
    def pesquisar(self, valor):
        atual = self.raiz
        while atual.valor != valor:
            if valor < atual.valor:
                atual = atual.esquerda
            else:
                atual = atual.direita
            if atual == None:
                return None
        return atual
    
                    

# Inserção e visualização

arvore = ArvoreBinariaBusca()

arvore.inserir(53)
arvore.inserir(30)
arvore.inserir(14)
arvore.inserir(39)
arvore.inserir(9)
arvore.inserir(23)
arvore.inserir(34)
arvore.inserir(49)
arvore.inserir(72)
arvore.inserir(61)
arvore.inserir(84)
arvore.inserir(79)

print(arvore.raiz.esquerda.valor)
print(arvore.raiz.direita.valor)

arvore.inserir(89)

print(arvore.ligacoes)

# Pesquisar
print(arvore.pesquisar(39))

print(arvore.pesquisar(84))

print(arvore.pesquisar(100))

if arvore.pesquisar(84) == None:
    print('Elemento não localizado.')
else:
    print('Elemento localizado.')