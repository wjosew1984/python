def carga():
    dicc=open("diccionario.txt","a")
    responde="si"
    while responde=="si":
        i=input("ingrese palabra en ingles: ")
        e=input("ingrese su trad: ")
        dicc.write(i+":"+e+"\n")
        responde=input("desea seguir cargando? si/no")
    dicc.close()

def listar():
    dicc=open("diccionario.txt")
    for dato in dicc:
        i,e=dato.strip().split(":")
        print(i,e)
    dicc.close()

def buscar():
    dicc=open("diccionario.txt")
    b=input("ingrese palabra en ingles: ")
    for dato in dicc:
        dato=dato.strip().split(":")
        if dato[0]==b:
            print(dato[1])
        else:
            print("no se encontró")
    dicc.close()

carga()
listar()
buscar()
