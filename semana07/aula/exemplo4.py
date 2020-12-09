# ler 4 números. exibir a quantidade de valores "positivo (acima de zero)"

qtde = 0
for i in range(4):
    numero = int(input(f"Informe o {i + 1} valor: "))
    if (numero > 0):
        qtde += 1

print("Quantidade =", qtde)
