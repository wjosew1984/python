numero1 = int(input("Introduce el primer numero: "))
numero2 = int(input("Introudce el segundo numero: "))

for n in range(numero1, numero2+1):
    if n % 2 == 0:
        print(n)