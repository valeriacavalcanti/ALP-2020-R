soma = 0

# exibir 4 vezes "IFPB"
for i in range(4):
    print("IFPB")

# pedir 3 números
for i in range(1, 4):
    numero = int(input(f"Informe {i}º valor: "))

# exibir os números pares entre 2 e 10
for i in range(2, 11, 2):
    print(i, end=" ")

print("")

# exibir os números entre 4 e 0
for i in range(4, -1, -1):
    print(i)
