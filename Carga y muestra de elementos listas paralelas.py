#1-cargar articulos y precios
#2-imprimir nombres con precios
#3-imprimir nombre con precio mayor
#4-ingresar por teclado un importe y luego mostrar todos los articulos con un precio menor o igual al valor ingresado.

def carga():
    art=[]
    prec=[]
    for x in range(2):
        f=str(input("Ingrese nombre: "))
        art.append(f)
        v=int(input("Ingrese precio: "))
        prec.append(v)
    return(art,prec)

def prin(art,prec):
    print(art,prec)

def may(art,prec):
    k = 0
    for x in range(len(prec)):
        if prec[x]<k:
            k=(prec[x])
    print("El precio mas elevado es: ",prec[x],art[x])


def ingre(art,prec):
    a=int(input("Ingrese precio y le mostraré articulos con precio similar: "))
    for x in range(len(prec)):
        if a<=prec[x]:
            print(art[x],prec[x])
        print("Disculpe, no se encuentra el producto solicitado.")

articulo,precio=carga()
muestralista=prin(articulo,precio)
precmayor=may(articulo,precio)
ingresaprec=ingre(articulo,precio)
