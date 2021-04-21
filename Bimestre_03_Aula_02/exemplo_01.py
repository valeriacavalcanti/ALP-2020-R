soma = 0
qtde_impar = 0
numeros = [0] * 10

for i in range(10):
    numeros[i] = int(input('Número: '))
    soma += numeros[i]
    if (numeros[i] % 2 == 1):
        qtde_impar += 1

print('Soma =', soma)
print('Média =', soma/10)
print('Quantidade ímpar = ', qtde_impar)
#print(numeros)

for i in range(len(numeros)):
    if (numeros[i] % 2 == 1):
        print(numeros[i])

'''
CASO DE TESTE
15 20 35 40 55 60 75 80 95 100
soma = 550
média = 55
quantidade ímpar = 5
'''
