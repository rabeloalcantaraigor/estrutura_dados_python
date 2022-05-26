lista1=[]

for x in range(1,6):
    numeros=float(input('Escreva os números: '))
    lista1.append(numeros)
    
print(lista1)

i=0
soma=0
for y in range(len(lista1)):
    soma=soma+lista1[i]
    i+=1
    
print(soma)
    