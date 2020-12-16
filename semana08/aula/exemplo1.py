"""
Ler vários números, vai encerrar quando for digitado
valor 0 (zero).
Ao final, informe quantos números foram lidos.
"""

qtde = 0
numero = int(input("Informe um valor: "))

while (numero != 0):
    qtde += 1
    numero = int(input("Informe um valor: "))

print("Quantidade de números =", qtde)
