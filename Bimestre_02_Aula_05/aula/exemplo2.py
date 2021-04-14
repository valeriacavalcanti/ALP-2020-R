qtde = 0

while (True):
    numero = int(input("Valor: "))

    if (numero != 0):
        qtde += 1
    else:
        break

print("Quantidade =", qtde)
