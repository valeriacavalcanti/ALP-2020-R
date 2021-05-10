minutos = int(input("Minutos consumidos: "))

if (minutos <= 100):
    p1 = 100
else:
    p1 = 100 + (minutos - 100) * 1

if (minutos <= 200):
    p2 = 180
else:
    p2 = 180 + (minutos - 200) * 0.8

if (minutos <= 300):
    p3 = 240
else:
    p3 = 240 + (minutos - 300) * 0.6

if (p1 < p2):
    print('Plano: Pouca Conversa')
elif (p1 == p2):
    print('Plano: Boa conversa')
elif (p2 < p3):
    print('Plano: Boa conversa')
elif (p2 >= p3):
    print('Plano: Falo muito')
