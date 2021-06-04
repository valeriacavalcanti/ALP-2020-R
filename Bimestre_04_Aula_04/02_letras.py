frase = input('Frase: ')
letras = []

for s in frase:
    if ((s >= 'a' and s <= 'z') or (s >= 'A' and s <= 'Z')) and (s not in letras):
        letras.append(s)

print(letras)
