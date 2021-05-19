qtde = 0
numero = input('Número: ')


eh_numerico = True
for i in range(len(numero)):
    if (numero[i] < '0') or (numero[i] > '9'):
        eh_numerico = False
        break

if (eh_numerico == True):
    print('Número inteiro')
else:
    print('Não é número inteiro')

print(numero.isdigit())

for i in range(len(numero)):
    if (numero[i] == '0'):
        qtde += 1

print('qtde =', qtde)
quantidade = numero.count('0')
print(quantidade)
