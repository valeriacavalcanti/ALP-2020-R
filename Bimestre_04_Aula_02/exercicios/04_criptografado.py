palavra = input('Palavra: ')
vogais = 'aeiouAEIOU'

for i in range(len(vogais)):
    palavra = palavra.replace(vogais[i], '*')

print(palavra)
