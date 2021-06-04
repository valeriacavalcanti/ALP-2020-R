from random import shuffle

def embaralhar(st):
    palavras = st.split()
    shuffle(palavras)
    nova = ''
    for p in palavras:
        nova += p + ' '
    return nova

nome = input('Frase: ')
print(embaralhar(nome))
