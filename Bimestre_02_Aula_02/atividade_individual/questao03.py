qt_sorv = int(input('Sorvete: '))
qt_suco = int(input('Suco: '))
qt_past = int(input('Pastel: '))
qt_brig = int(input('Brigadeiro: '))

total = qt_sorv * 2.5
total += qt_suco * 3
total += qt_past * 10.5
total += qt_brig * 4

# mais duas formas de obter o total

# total = qt_sorv * 2.5 + qt_suco * 3 + qt_past * 10.5 + qt_brig * 4

# total = (qt_sorv * 2.5) + (qt_suco * 3) + (qt_past * 10.5) + (qt_brig * 4)

print('Total:', total)

# precisão: duas casas após o ponto
print('Total: {:.2f}'.format(total))