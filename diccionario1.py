productos={"manzanas":50,"peras":20,"limon":10}
print(productos)
for clave in productos:
    print(clave,productos[clave])
    
productos={}
for x in range(3):
    prod=str(input("ingrse producto: "))
    prec=int(input("ingrese precio: "))
    productos[prod]=prec
print (productos)
