tamanho = float(input("Digite o tamanho em metros quadrados: "))

if tamanho % 52 != 0:
    latas = int(tamanho/52)+1
    preco = latas * 80
else:
    latas = tamanho / 52
    preco = latas * 80
print("%d latas a um custo de: %.2f " %(latas,preco))    
    


    
    
              
          
              
