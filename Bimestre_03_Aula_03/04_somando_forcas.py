# declarar as matrizes
matriz1 = []
for i in range(6):
    matriz1.append([0] * 4)

matriz2 = []
for i in range(6):
    matriz2.append([0] * 4)

matriz_soma = []
for i in range(6):
    matriz_soma.append([0] * 4)

# ler os dados das matrizes
for i in range(6):
    for j in range(4):
        matriz1[i][j] = int(input("Matriz1 {} {}: ".format(i, j)))

for i in range(6):
    for j in range(4):
        matriz2[i][j] = int(input("Matriz2 {} {}: ".format(i, j)))


# calculando a soma das matrizes 1 e 2
for i in range(6):
    for j in range(4):
        matriz_soma[i][j] = matriz1[i][j] + matriz2[i][j]

print(matriz_soma)
