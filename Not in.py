letras = []
i = 0
cont = 0

while i < 5:
    letras.append(input("Letra: "))

    if letras[i] not in 'aeiou':
        cont += 1
    i += 1
print("Foi digitado %d consoantes "%cont)
