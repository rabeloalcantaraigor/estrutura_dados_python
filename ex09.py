import numpy as np
matriz = np.array([[3,4,1],[3,1,5]])
print(matriz)

resultado=0
for i in range(0,2):
    for j in range(0,3):
        print(matriz[i][j])
        resultado=resultado+matriz[i][j]
        
print(resultado)