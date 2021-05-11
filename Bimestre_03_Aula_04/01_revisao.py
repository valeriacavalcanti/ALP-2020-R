qtde = soma = qtde_acima = 0

preco = float(input("Valor: "))
while (preco >= 0):
    qtde += 1
    soma += preco
    if (preco > 100):
        qtde_acima += 1
    preco = float(input("Valor: "))

if (qtde > 0):
    print('Valor médio:', soma/qtde)
    print('Quantidade acima de 100:', qtde_acima)
else:
    print('Não foi digitado valor válido')
