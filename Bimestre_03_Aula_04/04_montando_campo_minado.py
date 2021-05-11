# montar o tabuleiro
tabuleiro = []
for i in range(8):
    tabuleiro.append([0] * 8)

# inserir as peças
for i in range(10):
    print('Peça {}'.format(i))
    linha = int(input('Linha: '))
    coluna = int(input('Coluna: '))
    tabuleiro[linha][coluna] = 1

# exibir o tabuleiro
for i in range(8):
    print(tabuleiro[i])
