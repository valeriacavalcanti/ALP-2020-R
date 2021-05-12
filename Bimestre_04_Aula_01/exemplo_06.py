# estatísticas da string

st = 'abc.ABC!123 ?'

qtde_mai = 0
qtde_min = 0
qtde_num = 0
qtde_esp = 0

for s in st:
    if (s >= 'A') and (s <= 'Z'):
        qtde_mai += 1
    elif (s >= 'a') and (s <= 'z'):
        qtde_min += 1
    elif (s >= '0') and (s <= '9'):
        qtde_num += 1
    else:
        qtde_esp += 1

print(qtde_mai)
print(qtde_min)
print(qtde_num)
print(qtde_esp)
