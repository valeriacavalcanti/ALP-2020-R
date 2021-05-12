palavra = input('Palavra: ')
print(type(palavra), palavra)
print(len(palavra))

for i in range(len(palavra)):
    print(palavra[i])

# ord: retorna o código decimal de um símbolo
# chr: retorna o símbolo de um código decimal

print(ord('A'))
print(chr(65))
