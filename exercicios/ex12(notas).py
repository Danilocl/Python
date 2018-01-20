nota = []
r = 0
x = 0
media = 0
while x < 4:
    r = float(input("Nota: "))
    nota.append(r)
    media = media+r
    x += 1

print("Notas:",nota)
print("Média das notas",media/4)



