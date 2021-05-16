eh_numero = True
valor = input('Valor: ')

for s in valor:
    if (s < '0') or (s > '9'):
        eh_numero = False
        break

if (eh_numero == True):
    print('É número')
else:
    print('Não é número')
