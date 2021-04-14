salario = float(input("Informe seu salário: "))

if (salario < 500):
    #salario = salario + (salario * 10 / 100)
    #salario += (salario * 10 / 100)
    #salario += (salario * 0.1)
    #salario *= 1.1
    bonus = salario * 0.1
    salario = salario + bonus

print('Salario =', salario)
