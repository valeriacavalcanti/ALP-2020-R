def somar(lista):
    total = 0
    # variável com ESCOPO local
    minha_variavel = True
    for num in lista:
        total += num
    return total

def media(lista):
    minha_variavel = 0
    return somar(lista)/len(lista)

def acima(lista):
    qtde = 0
    minha_variavel = 12.3
    media_numeros = media(lista)
    for num in lista:
        if (num > media_numeros):
            qtde += 1
    return qtde

# PROGRAMA PRINCIPAL

# ler 10 valores
numeros = []
for i in range(10):
    numeros.append(int(input('Valor: ')))

# soma 10 valores
print(somar(numeros))

# média dos 10 valores
print(media(numeros))

# qde acima da média
print(acima(numeros))
