m1=float(input('Digite nota 1: '))
m2=float(input('Digite nota 2: '))
m3=float(input('Digite nota 3: '))

media = (m1 + m2 + m3)/3

if 0 <= media <= 4:
    print(f'Aluno está reprovado, nota: {media}')
    
elif 4.1 <= media < 6:
    exame = float(input('Digite a nota de exame: '))
    if exame >= 6:
        print(f'Aluno aprovado, nota: {exame}')
    else:
        print('Aluno reprovado')

elif media >= 6:
    print(f'Aluno está aprovado, nota: {media}')
    
