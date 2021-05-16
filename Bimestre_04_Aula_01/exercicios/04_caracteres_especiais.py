qtde_esp = 0

frase = input('Frase: ')

for s in frase:
    if not (s >= 'a' and s <= 'z') and\
            not (s >= 'A' and s <= 'Z') and\
            not(s >= '0' and s <= '9'):
        qtde_esp += 1

print('Quantidade:', qtde_esp)
