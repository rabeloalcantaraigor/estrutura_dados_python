
# Exercício de recursão para fatorial e exponencial

def fatorial_n(n):
    if n == 0 or n == 1:
        return 1
    
    return n * fatorial_n(n - 1)

print(fatorial_n(5))
   
def exponencial(b, e):
    if e == 0:
        return 1
    
    if b < 0 or e < 0:
        return None
    
    return b * exponencial(b,e - 1)

print(exponencial(3,3))
    