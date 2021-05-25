apenas_letras = 0
acima_dez = 0

palavra = input('Palavra: ')

while(palavra.upper() != 'FIM'):
    if (palavra.isalpha()):
        apenas_letras += 1
    if (len(palavra) > 10):
        acima_dez += 1
    palavra = input('Palavra: ')

print('Apenas letras:', apenas_letras)
print('Acima de 10 caracteres:', acima_dez)
