class Aluno:
    def __init__(self, nome, nota1, nota2): #Contrutor
        self.nome=nome #Atributo
        self.nota1=nota1 #Atributo
        self.nota2=nota2 #Atributo
        self.media=0 #Atributo
        
    def calcula_media(self): #Métodos
        self.media=(self.nota1+self.nota2)/2
        return self.media
    
    def mostra_dados(self): #Métodos
        return f'Aluno(a): {self.nome} e média: {self.media}'
    
    def verifica_aprovado_reprovado(self): #Métodos
        if self.media >= 6:
            return 'Aluno(a) Aprovado!'     
        else:
            return 'Aluno(a) Reprovado.'
        
aluno1=Aluno('Igor', 3, 8)
aluno2=Aluno('Giuliana', 9.5, 10)

print(aluno2.calcula_media())
print(aluno2.mostra_dados())
print(aluno2.verifica_aprovado_reprovado())