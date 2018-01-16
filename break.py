soma = 0

while True:

    resp = int(input("Digite o número especial: "))    
    if resp == 0:
        break
    soma = resp + soma
    print("soma: %d"%soma)
    
