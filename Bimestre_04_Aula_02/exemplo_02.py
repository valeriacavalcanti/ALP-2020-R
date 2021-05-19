numeros = input("Três valores: ")

print(numeros)
print(numeros.split())
print(numeros.split('/'))

dia, mes, ano = input('Data: ').split('/')

dia = int(dia)
mes = int(mes)
ano = int(ano)

print(type(dia), dia)
print(type(mes), mes)
print(type(ano), ano)

# nao funciona!
#dia, mes, ano = int(input('Data: ').split('/'))
#dia, mes, ano = int(input('Data: ')).split('/')
