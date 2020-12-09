soma = 0

for i in range(10):
    numero = int(input(f"Informe o {i + 1}º valor: "))
    #soma = soma + numero
    soma += numero

print("A soma dos números é", soma)
print(f"A soma dos números é {soma}") #interpolação
print("A soma dos números é {}".format(soma))
