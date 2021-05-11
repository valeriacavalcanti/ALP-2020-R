qtde = soma = 0
notas = []

# declarar a matriz
for i in range(4):
    notas.append([0] * 3)

# preencher a matriz com as notas dos alunos
for i in range(4):
    for j in range(3):
        notas[i][j] = int(input("Aluno {} - nota {}: ".format(i + 1, j + 1)))
        soma += notas[i][j]

# Ler o valor da média da instituição
media = int(input("Média: "))

# verificar quais alunos possuem nota acima da média
for i in range(4):
    tem_nota_acima_da_media = False
    for j in range(3):
        if (notas[i][j] > media):
            tem_nota_acima_da_media = True
            break
    if (tem_nota_acima_da_media == True):
        qtde += 1

print('Quantidade de alunos com nota acima da média:', qtde)
