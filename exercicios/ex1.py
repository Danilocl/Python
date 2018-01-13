
try:

    carro = int(input("Em que velocidade o carro estava ? "))
except ValueError:
        print('Somente números')        
if carro > 110:    
    multa = (carro - 110)*5
    print("Você foi multado em: %.2f" %multa)
else:
    print('Prossiga')
    
    
        
    
