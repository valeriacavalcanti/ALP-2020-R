nomes = []
idades = []
soma = 0

for i in range(8):
    nomes.append(input('Nome: '))
    idades.append(int(input('Idade: ')))
    soma += idades[i]

media = soma/8

print('Pessoas com idades acima da média do grupo.')
for i in range(8):
    if (idades[i] > media):
        print(idades[i])
