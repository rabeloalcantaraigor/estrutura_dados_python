def tempo_velocidade():
    tempo=float(input('Digite o tempo gasto: '))
    velocidade= float(input('Digite a velocidade: '))
    
    tempo_velocidade={
        'tempo':tempo,
        'velocidade':velocidade
    }
    
    return tempo_velocidade

x=tempo_velocidade()

def calcular_distancia(**tempo_velocidade):
    d=tempo_velocidade['tempo']*tempo_velocidade['velocidade']
    
    return d

distancia=calcular_distancia(**x)

def qte_litros_usados(distancia):
    litros_usados=distancia/12
    return litros_usados

def apresenta_resultados(distancia, tempo, velocidade, litros_usados):
    return f'Percorreu a distância de {distancia} km com {litros_usados} L no tempo de {tempo} h e velocidade {velocidade} km/h.'

tempo=x['tempo']
velocidade=x['velocidade']

litros=qte_litros_usados(distancia)
print(apresenta_resultados(distancia, tempo, velocidade, litros))

