ca=int(input("ingrese la cantidad de alumnos que viajaran: "))
if 0>=30:
    precio=4000
else:
    if 30>=49:
        precio=(95*ca)
    else:
        if 50>=99:
            precio=(70*ca)
        else:
            precio=(50*ca)
precioind=precio/ca
print("el costo total del viaje es: $",precio," y el precio por alumno es de: $",precioind)
        
