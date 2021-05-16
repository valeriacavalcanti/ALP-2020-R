qtde = 0
frase = input('Frase: ')

for s in frase:
    if (s >= 'a') and (s <= 'z'):
        qtde += 1

print('Quantidade:', qtde)
