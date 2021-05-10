maior_nome = nome = input('Nome: ')
maior_altura = altura = float(input('Altura: '))
while (altura > 0):
    if (altura > maior_altura):
        maior_nome, maior_altura = nome, altura
    nome = input('Nome: ')
    altura = float(input('Altura: '))

print('Nome da pessoa mais alta:', maior_nome)
