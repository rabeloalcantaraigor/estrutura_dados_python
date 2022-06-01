
# Recursão aula 1

for _ in range(5):
    print('Recursão')

print()
    
def recursao(i):
    print('Recursão')
    i+=1
    if i == 5:
        return
    else:
        recursao(i)

recursao(0)