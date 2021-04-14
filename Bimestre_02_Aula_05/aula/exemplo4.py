"""
   100 chocolates para distribuir entre VÁRIAS pessoas.
   Ao final, exiba quantas pessoas foram beneficiadas.
"""

estoque = 100
qtde = 0

while (True):
    if (estoque > 0):
        pedido = int(input("Informe a quantidade: "))
        if (pedido <= estoque):
            estoque -= pedido
            qtde += 1
        else:
            break
    else:
        break

print("Estoque:", estoque)
print("Pessoas:", qtde)

# 50 30 10 8 2 1 2
