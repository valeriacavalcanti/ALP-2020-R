def soma(lista):
    total = 0
    for i in range(len(lista)):
        total += lista[i]
    return total

def media(lista):
    return soma(lista)/len(lista)

def acima(lista):
    qtde = 0
    med = media(lista)
    for i in range(len(lista)):
        if (lista[i] > med):
            qtde += 1
    return qtde

def par(lista):
    qtde = 0
    for i in range(len(lista)):
        if (lista[i] % 2 == 0):
            qtde += 1
    return qtde

def ordenado(lista):
    for i in range(len(lista) - 1):
        if (lista[i] > lista[i + 1]):
            return False
    return True

# Programa Principal

numeros = [1,4,6,2,9,54,2,31,60]

print(soma(numeros))
print(media(numeros))
print(acima(numeros))
print(par(numeros))
print(ordenado(numeros))
