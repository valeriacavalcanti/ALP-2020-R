qtde = 0
soma = 0

for i in range(6):
    alunos = int(input(f"Quantidade de alunos da turma {i + 1}: "))
    soma += alunos
    for j in range(alunos):
        pontos = int(input("Quantidade de pontos: "))
        if ((pontos >= 20)and (pontos <= 40)):
            qtde += 1

print("Quantidade [20,40]:", qtde)
print("Total de estudantes entrevistados:", soma)
