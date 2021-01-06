#cargar por teclado y almacenar en una lsita las alturas de 5 personas y calcular promedio.
# contar cuantas personas son mas altas que el promedio y cuantas mas bajas.

n=[]
tot=0
for x in range(5):
    v=float(input("Ingrese estatura: "))
    n.append(v)
    tot=tot+n[x]
    prom=(tot/5)
print("El promedio es de: ",prom)
a=0
b=0
for x in range(5):
    if n[x] > prom:
        print(n[x]," Es mayor que el promedio.")
    else:
        print(n[x]," Es menor que el promedio.")

