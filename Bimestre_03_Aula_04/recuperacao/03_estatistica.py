lista = []
soma = qt_igual = qt_entre = 0

for i in range(10):
    lista.append(int(input('Valor: ')))
    soma += lista[i]
    if (lista[i] >= 10) and (lista[i] <= 100):
        qt_entre += 1

print('Soma:', soma)
media = soma/10
print('Valores abaixo da média: ', end='')
for i in range(10):
    if (lista[i] < media):
        print(lista[i], end=' ')
    if (i != 4) and (lista[i] == lista[4]):
        qt_igual += 1

print('\nQuantidade igual ao quinto:', qt_igual)
print('Quantidade entre [10,100]:', qt_entre)
