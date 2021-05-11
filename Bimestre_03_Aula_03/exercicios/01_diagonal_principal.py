matriz = []
for i in range(4):
    matriz.append([0] * 4)

for i in range(4):
    for j in range(4):
        matriz[i][j] = input("elemento {} {}: ".format(i, j))

print('Elementos da diagonal principal: ')
for i in range(4):
    print(matriz[i][i])
