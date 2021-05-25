qtde = 0
vogais = 'aeiouAEIOU'

frase = input('Frase: ')

for i in range(len(frase)):
    if (frase[i] in vogais):
        qtde += 1

print('Vogais:', qtde)
