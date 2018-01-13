num1 = float(input("Primeiro número: "))
num2 = float(input("Segundo número: "))
num3 = float(input("Terceiro número: "))

if num1 >= num2 and num1>= num3:
    print("O número %d é o maior" %num1)
elif num2 >= num3:
    print("O número %d é o maior" %num2)
else:
    print("O número %d é o maior" %num3)
