# Programa de uma menina de doze anos Criptografia César CEDET Decolar



print(chr(30000))

def esconde(msg):
    s = ''
    for c in msg:
        s += chr(ord(c) + 3000)
    return print(s)

def mostra(msg):
    s = ''
    for c in msg:
        s += chr(ord(c) - 3000)
    return s

teste = esconde('Python para zumbis')

print(mostra('ఈఱబఠధద௘నఙపఙ௘లభథచడఫ'))

