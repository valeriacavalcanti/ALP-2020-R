num = 32
lista1 = []
lista2 = [10,20,30,40,50,60]
lista3 = [0] * 10

print(lista1, len(lista1))
print(lista2, len(lista2))
print(lista3, len(lista3))

for i in range(len(lista2)):
    print(i, lista2[i])

print(lista2[1])
print(lista2[1:4]) # retorna uma sublista
print(lista2[1:])
print(lista2[:4])
