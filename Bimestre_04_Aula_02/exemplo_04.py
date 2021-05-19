def count(st, s):
    qtde = 0
    for i in range(len(st)):
        if (st[i] == s):
            qtde += 1
    return qtde

# PROGRAMA PRINCIPAL

frase = 'eu adoro python'
simbolo = 'p'

print(count(frase, simbolo))
