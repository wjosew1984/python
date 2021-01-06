productos={"manzanas":50,"peras":20,"limon":10}
print(productos)
for clave in productos:
    print(clave,productos[clave])

valor=input("ingrese un valor: ")
if valor in productos:
    print(productos[valor])
else:
    print("no se encuentra el producto")
