def quantidade_de_palavras(st):
    return st.count(' ') + 1

def quantidade_vogais(st):
    vogais = "aeiouAEIOU"
    qtde = 0
    for s in st:
        if (s in vogais):
            qtde += 1
    return qtde

def meu_print(st):
    for s in st:
        print(s, end=' ')
    print()

def exiba_ifpb():
    print("Instituto federal da paraiba")
    print("Campus João Pessoa")
    print("Jaguaribe")

def retorne_10():
    print("linha 1")
    return 10
    print("linha 2")

# programa principal

teste = "instituto federal da paraiba"

print(quantidade_de_palavras(teste))
print(quantidade_vogais(teste))
meu_print(teste)
exiba_ifpb()
print(retorne_10())
