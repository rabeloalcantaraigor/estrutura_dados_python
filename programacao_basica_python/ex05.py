media = 0
i=0
for x in range(1,6):
    notas = float(input(f'Escreva a nota {i+1}: '))
    media=media+notas
    i+=1
print(media/i)