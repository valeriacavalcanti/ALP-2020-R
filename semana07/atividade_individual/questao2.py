qtde = 0

for i in range(4):
    nota1 = float(input("Primeira nota: "))
    nota2 = float(input("Primeira nota: "))
    nota3 = float(input("Primeira nota: "))
    media = (nota1 + nota2 + nota3)/3
    if (media >= 7):
        qtde += 1

print("Quantidade aprovados =", qtde)
