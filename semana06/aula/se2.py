'''
 [0,100]    - 2 parcelas
 ]100, 200] - 3 parcelas
 ]200, 400] - 6 parcelas
 ]400, ...] - 10 parcelas
'''

compra = float(input('Informe o valor: '))

if (compra <= 100):
    print('2 parcelas')
elif (compra <= 200):
    print('3 parcelas')
elif (compra <= 400):
    print('6 parcelas')
else:
    print('10 parcelas')


if (compra <= 100):
    print('2 parcelas')
else:
    if (compra <= 200):
        print('3 parcelas')
    else:
        if (compra <= 400):
            print('6 parcelas')
        else:
            print('10 parcelas')
