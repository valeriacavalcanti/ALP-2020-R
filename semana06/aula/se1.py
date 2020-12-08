
media = input('Informe sua média: ')
media = int(media)

# operadores relacionais: > < >= <= == !=

'''
Aprovado: media >= 70
Final: media >= 40
Reprovado: media < 40
'''

if (media >= 70):
    print('Aprovado')
else:
    if (media >= 40):
        print('Final')
    else:
        print('Reprovado')

# ----------------------------

if (media >= 70):
    print('Aprovado')
elif (media >= 40):
    print('Final')
else:
    print('Reprovado')
