class Pessoa():
    pass

pessoa1 = Pessoa()

pessoa1.nome = 'Igor'
pessoa1.idade = 26
pessoa1.documentos = {
    'Identidade': 2989973,
    'cpf': 15632258157,
}
pessoa1.pais = ['Veudaci', 'Tereza']
print(pessoa1.nome)
print(pessoa1.idade)
print(pessoa1.documentos)
print(pessoa1.pais)