qtde_acima_20 = 0
soma = 0
qtde = 0

num = int(input('Número: '))
while(num != 0):
    qtde += 1
    soma += num
    if (num > 20):
        qtde_acima_20 += 1
    num = int(input('Número: '))

if (qtde > 0):
    media = soma / qtde
    print(media)
else:
    print('não existe média')

print(num)
print(soma)
print(qtde)
print(qtde_acima_20)
