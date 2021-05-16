soma = 0
qtde = 0

for i in range(200):
    valor = float(input('Valor: '))
    soma += valor
    if (valor > 1000):
        qtde += 1

print('Valor total:', soma)
print('Valor médio:', soma/200)
print('Quantidade com valor acima de R$ 1000,00:', qtde)
