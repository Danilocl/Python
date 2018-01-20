x = '0123456789'

#Irá imprimir do 0 ao número anterior ao 2
print(x[0:7])

#quando o primeiro é omitido, ele começa do zero
print(x[:5])
# quando o último é omitido, ele vai até o ultimo número
print(x[5:])
#-1 é um número anterior ao último
print(x[0:-1])
#-2 é dois números anteriores ao último
print(x[4:-2])
#a porra toda
print(x[:])

'''Fatiamento de texto'''

texto = 'batatinha quando nasce'
print(texto)
print(texto[::2])
print(texto[::-1])




