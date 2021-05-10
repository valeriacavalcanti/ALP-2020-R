numeros = []

while (len(numeros) < 6):
    num = int(input('Número: '))
    if (num not in numeros):
        numeros.append(num)

print(numeros)
