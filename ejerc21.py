c=1
ta=0
tna=0
cp=int(input("Ingrese la cantidad de piezas: "))
while c<=cp:
    lon=float(input("ingrese la longitud de la pieza: "))
    if lon>=1.20 and lon<=1.30:
        ta=ta+1
    else:
        tna=tna+1
    c=c+1
print("Aptos: ",ta," y no aptos: ",tna)
