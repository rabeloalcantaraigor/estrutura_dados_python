
# Terminologia de árvores

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
    
    # Raiz, esquerda, direita
    def pre_ordem(self, no):
        if no != None:
            print(no.valor)
            self.pre_ordem(no.esquerda)
            self.pre_ordem(no.direita)
    
    # Esquerda, raiz, direita
    def em_ordem(self, no):
        if no != None:
            self.em_ordem(no.esquerda)
            print(no.valor)
            self.em_ordem(no.direita)
            
    # Esquerda, direita, raiz
    def pos_ordem(self, no):
        if no != None:
            self.pos_ordem(no.esquerda)
            self.pos_ordem(no.direita)
            print(no.valor)
    
    def excluir(self, valor):
        if self.raiz == None:
            print('A árvore está vazia.')
            return
        
        # Encontrar o nó
        atual = self.raiz
        pai = self.raiz
        e_esquerda = True
        while atual.valor != valor:
            pai = atual
            # Esquerda
            if valor < atual.valor:
                e_esquerda = True
                atual = atual.esquerda
            # Direita
            else:
                e_esquerda = False
                atual = atual.direita
            if atual == None:
                return False
            
        # O nó a ser apagado é uma folha
        if atual.esquerda == None and atual.direita == None:
            if atual == self.raiz:
                self.raiz == None
            elif e_esquerda == True:
                self.ligacoes.remove(str(pai.valor) + '->' + str(atual.valor))
                pai.esquerda = None
            else:
                self.ligacoes.remove(str(pai.valor) + '->' + str(atual.valor))
                pai.direita = None
        
        # O nó a ser apagado não possui filho na direita
        elif atual.direita == None:
            
            self.ligacoes.remove(str(pai.valor) + '->' + str(atual.valor))
            self.ligacoes.remove(str(atual.valor) + '->' + str(atual.esquerda.valor))
            
            if atual == self.raiz:
                self.raiz = atual.esquerda
                
                self.ligacoes.append(str(raiz.valor) + '->' + str(atual.esquerda.valor))
                
            elif e_esquerda == True:
                pai.esquerda = atual.esquerda
                
                self.ligacoes.append(str(pai.valor) + '->' + str(atual.esquerda.valor))
                
            else:
                pai.direita = atual.esquerda
                
                self.ligacoes.append(str(pai.valor) + '->' + str(atual.esquerda.valor))
        
        # O nó a ser apagado não possui filho na esquerda
        elif atual.esquerda == None:
            
            self.ligacoes.remove(str(pai.valor) + '->' + str(atual.valor))
            self.ligacoes.remove(str(atual.valor) + '->' + str(atual.direita.valor))
            
            if atual == self.raiz:
                
                self.ligacoes.append(str(raiz.valor) + '->' + str(atual.direita.valor))
                
                self.raiz = atual.direita
            elif e_esquerda == True:
                
                self.ligacoes.append(str(pai.valor) + '->' + str(atual.direita.valor))
                
                pai.esquerda = atual.direita
            else:
                
                self.ligacoes.append(str(pai.valor) + '->' + str(atual.direita.valor))
                
                pai.direita = atual.direita
        
        # O nó possui dois filhos
        else:
            sucessor = self.get_sucessor(atual)
            
            self.ligacoes.remove(str(pai.valor) + '->' + str(atual.valor))
            self.ligacoes.remove(str(atual.direita.valor) + '->' + str(sucessor.valor))
            self.ligacoes.remove(str(atual.valor) + '->' + str(atual.esquerda.valor))
            self.ligacoes.remove(str(atual.valor) + '->' + str(atual.direita.valor))
            
            if atual == self.raiz:
                
                self.ligacoes.append(str(self.raiz.valor) + '->' + str(sucessor.valor))
                
                self.raiz = sucessor
                
            elif e_esquerda == True:
                
                self.ligacoes.append(str(pai.valor) + '->' + str(sucessor.valor))
                
                pai.esquerda = sucessor
            else:
                
                self.ligacoes.append(str(pai.valor) + '->' + str(sucessor.valor))
                
                pai.direita = sucessor
            
            self.ligacoes.append(str(sucessor.valor) + '->' + str(atual.esquerda.valor))
            self.ligacoes.append(str(sucessor.valor) + '->' + str(atual.direita.valor))
            
            sucessor.esquerda = atual.esquerda
            
        return True
    
    def get_sucessor(self, no):
        pai_sucessor = no
        sucessor = no
        atual = no.direita
        while atual != None:
            pai_sucessor = sucessor
            sucessor = atual
            atual = atual.esquerda
        
        if sucessor != no.direita:
            pai_sucessor.esquerda = sucessor.direita
            sucessor.direita = no.direita
        
        return sucessor
        
                    

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
    
# Travessia

arvore.pre_ordem(arvore.raiz)

print()

arvore.em_ordem(arvore.raiz)

print()

arvore.pos_ordem(arvore.raiz)

# Excluir

arvore.excluir(9)

print(arvore.ligacoes)

arvore.excluir(79)

print(arvore.ligacoes)

arvore.excluir(89)

print(arvore.ligacoes)


arvore.excluir(100)

print(arvore.ligacoes)

arvore.excluir(84)

print(arvore.ligacoes)

arvore.excluir(9)

print(arvore.ligacoes)

arvore.excluir(14)

print(arvore.ligacoes)

print(arvore.get_sucessor(arvore.raiz).valor)

arvore.excluir(72)

print(arvore.ligacoes)

arvore.excluir(30)

print(arvore.ligacoes)