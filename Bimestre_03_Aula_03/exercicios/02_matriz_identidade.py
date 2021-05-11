qtde_0 = qtde_1 = 0

# declarar a matriz
matriz = []
for i in range(5):
    matriz.append([0] * 5)

# preencher a matriz e contar os 0(zero) dos elementos fora da diagonal principal
# contar os 1 (um) dos elementos da diagonal principal
for i in range(5):
    for j in range(5):
        matriz[i][j] = int(input("elemento {} {}: ".format(i, j)))
        if (i == j) and (matriz[i][j] == 1):
            qtde_1 += 1
        elif (i != j) and (matriz[i][j] == 0):
            qtde_0 += 1

# verificar as condições da matriz identidade
if (qtde_1 == 5) and (qtde_0 == 20):
    print('Matriz identidade')
else:
    print('Outro tipo de matriz')
