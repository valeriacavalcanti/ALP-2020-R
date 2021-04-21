lista = [10,20,30,10,40]

print(lista)

lista.remove(20)
print(lista)

lista.remove(10)
print(lista)

if (100 in lista):
    lista.remove(100)
else:
    print('nao tem 100')

print(lista)
