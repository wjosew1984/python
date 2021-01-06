
def dicc():
    leer=open("diccionario.txt","a")
    preg="S"
    while preg=="S":
        ing=input("palabra en ingles:")
        esp=input("palabra en español:")
        leer.write(ing+"-"+esp+"\n")
        preg=input("desea seguir cargando? S/N").upper()
    leer.close()
    
def listarr():
    leer=open("diccionario.txt")
    lista={}
    for x in leer:
        w=x.strip()
        dicc=w.split("-")
        lista[dicc[0]]=dicc[1]
    for x in lista:
        print(x,"---", lista[x])        
def busc():
    leer=open("diccionario.txt")
    lista=[]
    for x in leer:
        w=x.strip()
        diic,dicc=w.split("-")
        lista.append((diic,dicc))            
    bus=input("ingrese palabra que desea buscar: ")
    t="no se encuentra"
    for x in range(len(lista)):
        if bus==lista[x][0] or bus==lista[x][1]:
            t=lista[x][0]+":"+lista[x][1]
    print(t)
           
def menu():
    opcion=9
    while opcion != 0:
        print("menu")
        opcion=int(input("1-cargar diccionario \n 2-listar diccionario \n 3-buscar palabra \n 0-salir \n "))
        if opcion==1:
            dicc()
        else:
            if opcion==2:
                listarr()
            else:
                if opcion==3:
                    busc()
                else:
                    if opcion !=0:
                        print("error")

menu()



        
    
