soma = 0
qtde_acima_20 = 0

qtde = int(input('Quantidade: '))

#for i in range(4):
for i in range(qtde):
    num = int(input('Número: '))
    soma = soma + num # soma += num
    if (num > 20):
        qtde_acima_20 += 1
        # qtde_acima_20 = qtde_acima_20 + 1

print(soma)
print(qtde_acima_20)
