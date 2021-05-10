qtde = 0
numeros = []

for i in range(10):
    num = int(input("Número: "))
    numeros.append(num)

for i in range(9):
    if (numeros[i] == numeros[9]):
        qtde += 1

print('Quantidade =', qtde)
