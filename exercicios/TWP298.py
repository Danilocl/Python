import random
#Gere uma lista de 15 aleatórios distintos

lista = []

while len(lista) < 15:
    x = random.randint(1,100)
    if x not in lista:
        lista.append(x)
lista.sort()
print(lista)