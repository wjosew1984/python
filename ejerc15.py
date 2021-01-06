cantp=int(input("ingrese la cantidad de personas: "))
km=int(input("ingrese la cantidad de km por recorrer: "))
micro=input("ingrese el tipo de micro: a, c ó b ")
if micro=="a":
    pkg=km*2
else:
    if micro=="b":
        pm=km*2*5
    else:
        pm=km*3
preciototal=pm*cantp
if cantp>20:
    precioind=preciototal/cantp
else:
    precioind=preciototal/20
print("el precio total del viaje es de: $",preciototal,"el precio individual es de: $",precioind)
        
