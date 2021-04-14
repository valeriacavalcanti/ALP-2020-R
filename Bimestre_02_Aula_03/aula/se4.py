
'''
    [0, 100]    -> nota válida
    ]..., 0[    -> nota inválida
    ]100, ...[  -> nota inválida
'''

nota = int(input("Informe sua nota: "))

if (nota >= 0) and (nota <= 100):
    print('Nota válida!')
else:
    print('Nota inválida')


if (nota < 0) or (nota > 100):
    print("Nota inválida")
else:
    print("Nota válida")
