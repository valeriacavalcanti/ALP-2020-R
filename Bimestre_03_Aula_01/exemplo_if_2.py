'''
obter o valor de uma compra
valor <= 100 : 2 parcelas
valor > 100 e valor <= 200 : 4 parcelas
acima 200: 6 parcelas
'''

valor = float(input("Valor: "))

if (valor <= 100):
    print('2 parcelas')
else:
    # certeza: valor > 100
    if (valor <= 200):
        print('4 parcelas')
    else:
        # certeza: valor > 200
        print('6 parcelas')

if (valor <= 100):
    print('2 parcelas')
elif (valor <= 200):
    print('4 parcelas')
else:
    print('6 parcelas')
