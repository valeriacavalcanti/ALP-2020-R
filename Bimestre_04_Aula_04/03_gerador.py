from random import randint

def gerador(qtde):
    senha = ''
    for i in range(qtde):
        senha += chr(randint(ord('A'), ord('Z')))
    return senha

# Programa Principal

print(gerador(4))
print(gerador(8))
print(gerador(12))
