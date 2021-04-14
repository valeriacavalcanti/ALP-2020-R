'''
    aprovado: media >= 70 e frequencia >= 75
    e: and
    ou: or
'''

media = int(input("Informe sua media: "))
freq = int(input("Informe sua frequencia: "))

if (media >= 70) and (freq >= 75):
    print('aprovado')
else:
    print('reprovado')
