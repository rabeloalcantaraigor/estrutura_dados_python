from operator import xor


tempo = float(input('Digite o tempo gasto na viagem: '))
velocidade = float(input('Digite a velocidade média: '))

distancia = tempo * velocidade
litros_usados = distancia / 12

print('velocidade média: ', velocidade)
print('tempo gasto na viagem: ', tempo)
print('distância percorrida ', distancia)
print('quantidade de litros: ', round(litros_usados, 1))