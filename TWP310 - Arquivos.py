arquivo = open('numeros.txt','w')
for linha in range(0,101):
    arquivo.write('%d\n'%linha)
arquivo.close()

