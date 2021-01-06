pfijo=50
ckg=int(input("ingrese cantidad de kg: "))
tipo=input("ingrese tipo de uva: ")
tam=int(input("ingrese el tamaño de uva: "))
if tipo=="a":
    if tam==1:
        total=(pfijo+0.20)*ckg
    else:
        total=(pfijo+0.30)*ckg
else:
    if tam==1:
        total=(pfijo-0.30)*ckg
    else:
        total=(pfijo-0.50)*ckg
print("el costo total es de: $",total)
    
