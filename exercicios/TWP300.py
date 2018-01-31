#Lista V Google Developer Day 2010

'''
Questão D. Daniela é uma pessoa muito supersticiosa. Para ela, um número é sortudo se ele contém o dígito 2 mas não o
dígito 7. Então, na opinião dela, quantos números sortudos existem entre 18644 e 33087, incluindo os extremos?
Resposta: 7995
'''

lista = [18644]
sorte = 2
x = 33087
b = 18644
while len(lista) <= x:
    if sorte in lista:
        b += 1
        lista.append(b)
    b += 1
