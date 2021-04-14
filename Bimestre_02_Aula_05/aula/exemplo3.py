"""
   100 chocolates para distribuir entre VÁRIAS pessoas.
   Ao final, exiba quantas pessoas foram beneficiadas.
"""

estoque = 100
qtde = 0

pedido = int(input("Informe a quantidade: "))

while ((estoque > 0) and (pedido <= estoque)):
    estoque -= pedido
    qtde += 1
    if (estoque > 0):
        pedido = int(input("Informe a quantidade: "))

print("Estoque:", estoque)
print("Pessoas:", qtde)

# 50 30 10 8 2 1 2
