meses = [0] * 12

for i in range(10):
    dia = int(input('Dia: '))
    mes = int(input('Mês: '))
    ano = int(input('Ano: '))
    meses[mes - 1] += 1

for i in range(12):
    print(i + 1, meses[i])
