qtde = 0
tabuleiro = []
for i in range(6):
    tabuleiro.append([0] * 6)

for i in range(20):
    linha = int(input('Linha: '))
    coluna = int(input('Coluna: '))
    if (tabuleiro[linha][coluna] == 0):
        tabuleiro[linha][coluna] = 1
        qtde += 1

print('Foram inseridas {} pecas no tabuleiro'.format(qtde))
for i in range(6):
    print(tabuleiro[i])
