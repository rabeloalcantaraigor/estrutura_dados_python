from numpy import append


try:
    lista=[]

    i=0
    while i < 2:
        valor=float(input('Digite os valores: '))
        lista.append(valor)
        i+=1
        
    divisao= lista[0]/lista[1]

except ValueError:
    print('Erro! Usuário digitou caractere.')
    
except ZeroDivisionError:
    print('Erro! Usuário digitou zero no denominador.')
    
except IndexError:
    print('Erro! Não existe esta posição na lista.')
    
except KeyboardInterrupt:
    print('Erro! Usuário interrompeu a execução.')

else:
    print(f'O valor da divisão é {divisao}')