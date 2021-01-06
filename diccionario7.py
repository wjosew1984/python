
def carga():
    responde="si"
    productos={}
    while responde=="si":
        codigo=input("ingrese codigo de producto: ")
        desc=input("ingrese nombre producto: ")
        prec=int(input("ingrese precio producto: "))
        stock=int(input("ingrese cantidad en stock: "))
        productos[codigo]=(desc,prec,stock)
        responde=input("desea cargar?(si/no)")
    return productos

def impr(productos):
    for codigo in productos:
        print("Codigo: {0}, nombre: {1}, precio: {2}, stock: {3}".format(codigo,productos[codigo][0],productos[codigo][1],productos[codigo][2]))

def consulta(productos):
    palabra=input("Ingrese codigo a buscar: ")
    if palabra in productos:
        print( "Nombre %s  Precio %d En stock %d"%(productos[palabra][0],productos[palabra][1],productos[palabra][2]))

        
def sinstock(productos):
    for codigo in productos:
        if productos[codigo][2]==0:
            print("No hay stock de: %s"%productos[codigo][0])
            

lista_productos=carga()
impr(lista_productos)
consulta(lista_productos)
sinstock(lista_productos)        
    
