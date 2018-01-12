carro = int(input("Em que velocidade o carro estava ? "))

if carro > 110:    
    multa = (carro - 110)*5
    print("Você foi multado em: ", multa)
else:
    print('Prossiga')
        
    
