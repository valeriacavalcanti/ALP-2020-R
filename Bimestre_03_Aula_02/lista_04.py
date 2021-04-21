lista = [10,20,10,30,10,10,40,10,50]

qtde = lista.count(10)
print(lista.count(10))

for i in range(qtde):
    lista.remove(10)

print(lista)
