'''split separa as palavras de acordo com espaço entre elas ou o parâmetro passado ao método
join junta os elementos de uma lista '''
txt = 'batatinha quando nasce'
print(txt.split())
data = '21/01/2018'
print(data.split('/'))
#não me rackeiem
ip = '192.168.1.186'
print(ip.split('.'))
paises = ['Brasil','Itália','Suíça']
print('/'.join(paises))

