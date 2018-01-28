
var = 10

def muda_imprime():
    global var
    var = 20
    print('variável %d dentro da função' %var)
print('variável %d antes de entrar na função' %var)
muda_imprime()
print('variável %d depois de entrar na função' %var)

