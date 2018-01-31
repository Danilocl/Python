n = int(input("n: "))

a, b, = 1 , 1
k = 1
d = 1
f = 5
r = 0
while k <= (n - 1)/2:
    a,b = b, a + b
    k = k + 1
    print(b)
a,b = b, a + b
r = int(input("Digite o próximo número: "))
while r == b and k <= n - 2:
    print(b)
    a,b = b, a + b
    r = int(input("Digite o próximo número: "))
    k = k + 1
            
    
    
    
    
    
    

