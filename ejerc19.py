tot=0
c=0
est=float(input("ingrese estatura: "))
while est>0:
    est=float(input("ingrese estatura: "))
    tot=tot+est
    print(est)
    c=c+1
if c==0:
    print("No hay estatura")
else:
    promedio=tot/c
    print("el promedio es de: ",promedio)
