qtde = 0

for i in range(10):
    print(f"Produto: {i + 1}")
    antes = float(input("Valor antes: "))
    depois = float(input("Valor depois: "))
    if (depois < antes):
        qtde += 1

print("Quantidade =", qtde)
