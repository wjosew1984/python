def mayor(t):
    m=len(t)
    return m
texto=str(input("ingrese texto:"))
a=mayor(texto)
texto=str(input("ingrese texto:"))
b=mayor(texto)
if a>b:
    print("El primer texto es el mas largo con: ",a)
else:
    print("El primer texto es el mas largo con: ",b)
