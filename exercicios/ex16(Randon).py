import random

word = input("Digite uma letra: ")


def embaralha(word):
    lista = list(word)
    random.shuffle(lista)
    print("lista: %s"%lista)
    return print("Sua nova palavra é: %s"%''.join(lista))

embaralha(word)

def choice():
    x = 0
    word = input("Digite uma palavra: ")
    lista = list(word)
    while x < len(word):
        print(random.choice(lista))
        x += 1
    return lista

choice()

def aleatorio():
    lista = []
    for k in range(15):
        lista.append(random.randint(10,100))
    print(lista)


aleatorio()