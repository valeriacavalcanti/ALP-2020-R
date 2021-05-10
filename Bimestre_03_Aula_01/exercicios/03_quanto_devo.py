soma = 0
acima = 0

for i in range(10):
    valor = float(input('Valor: '))
    soma += valor
    if (valor > 20):
        acima += 1

print('Valor médio:', soma/10)
print('Quantidade acima de R$ 20,00:', acima)
