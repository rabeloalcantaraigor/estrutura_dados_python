idade=int(input('Digite a idade da pessoa: '))

if idade >= 0 and idade <= 12:
    print('criança')

if idade >= 13 and idade <= 17:
    print('adolescente')
    
if idade >= 18:
    print('adulto')
    
if idade < 0:
    print('idade é inválida!')