# 4 alunos e 4 notas

matriz = []

for i in range(4):
    matriz.append([0] * 4)

print(matriz)

matriz[0][3] = 100
print(matriz)

matriz[3][0] = 100
print(matriz)

for i in range(4): #linhas
    for j in range(4): #colunas
        matriz[i][j] = 100

print(matriz)

# diagonal principal = 50

for i in range(4):
    matriz[i][i] = 50

print(matriz)
