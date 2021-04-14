antes = float(input("Informe o valor antes: "))
durante = float(input("Informe o valor durante: "))

if (antes > durante):
    reducao = ((antes - durante) / antes) * 100
    print(f'-{reducao}%')
else:
    aumento = ((durante - antes) / antes) * 100
    print(f'+{aumento}%')
