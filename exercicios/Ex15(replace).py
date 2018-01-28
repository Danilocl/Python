meses = ["janeiro","fevereiro","março","abril","junho",
         "julho","agosto","setembro","outubro","novembro","dezembro"]
dia,mes,ano = input("Data xx/xx/xxxx: ").split('/')
print("%s de %s %s"%(dia,meses[int(mes) - 1],ano))




