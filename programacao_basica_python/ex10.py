def ler_graus_selsius_em_fahrenheit():
    C = float(input('Informe a temperatura em ºC: ')) 
    return C

def calcular_graus_celsius_em_fahrenheit(C):
    F=(9*C+160)/5
    
    return F

graus=ler_graus_selsius_em_fahrenheit()
gcf=calcular_graus_celsius_em_fahrenheit(graus)

def mostra_graus_celsius_em_fahrenheit(gcf):
    return print(f'Temperatura em Fahrenheit {gcf}')

mostra_graus_celsius_em_fahrenheit(gcf)