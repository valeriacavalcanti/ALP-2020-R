st = 'abc.ABC!123 ?'
qtde = 0

# maiúsculo: A (65) - Z (90)
# minúsculo: a (97) - z (122)
# números: 0 (48) - 9 (57)

for i in range(len(st)):
    if (ord(st[i]) >= 65) and (ord(st[i]) <= 90):
        print(st[i])
        qtde += 1

print('Qtde =', qtde)

qtde = 0
for i in range(len(st)):
    if (st[i] >= 'A') and (st[i] <= 'Z'):
        print(st[i])
        qtde += 1

print('Qtde =', qtde)

qtde = 0
for s in st:
    if (s >= 'A') and (s <= 'Z'):
        print(s)
        qtde += 1

print('Qtde =', qtde)
