numeros = []
soma = qtde_acima = qtde_ultimo = 0

# leitura dos valores e soma
for i in range(10):
    numeros.append(int(input('Número: ')))
    soma += numeros[i]

# cálculo da média
media = soma/10

# descobrir os valores acima da média
for i in range(10):
    if (numeros[i] > media):
        qtde_acima += 1

# descobrir os valores iguais ao último número lido
for i in range(9):
    if (numeros[i] == numeros[9]):
        qtde_ultimo += 1


print('Média =', media)
print('Quantidade de números acima da média:', qtde_acima)
print('Quantidade de números com valor igual ao último:', qtde_ultimo)

# exibir os números com valores positivos
print('Números positivos: ', end='')
for i in range(10):
    if (numeros[i] > 0):
        print(numeros[i], end=' ')
print()
