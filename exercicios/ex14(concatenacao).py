'''faça um programa que leia uma palavra e troque as vogais por *'''

# O NOT IN VERIFICA CADA LETRA SEPARADAMENTE. SE HOUVER UMA ÚNICA CONSOANTE D NA PALAVRA, ELE NÃO ENTRARÁ NA CONDIÇÃO

palavra = input("Digite uma palavra: ")
troca = ''
con = ''
k = 0
i = 0

while i < len(palavra):
    if palavra[i] not in 'aeiou':
        con = con + palavra[i]
    i = i + 1
if palavra == con:
    print("A palavra %s não possui nenhuma vogal"%con)

while k < len(palavra):
    if palavra[k] in 'aeiou':
        troca = troca + '*'
    else:
        troca = troca + palavra[k]
    k = k + 1
print("A nova palavra é: %s"%troca)







