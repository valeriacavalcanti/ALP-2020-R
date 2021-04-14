num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
num3 = int(input('Terceiro número: '))

media = (num1 + num2 + num3) / 3

print('Média =', media)

# exibindo a média com duas casas após o ponto
print('Média = {:.2f}'.format(media))