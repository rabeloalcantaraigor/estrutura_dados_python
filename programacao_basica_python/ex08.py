alunos = {
    'Igor':8.5,
    'Giuliana':10.0,
    'Esdras':9.5
}

media=0
for nome, nota in alunos.items():
    print(nome, nota)
    media=media+nota

print(f'A média é {media/len(alunos)}')
    