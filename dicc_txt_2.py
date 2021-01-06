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
    nuevo={}
    for dato in dicc:
        ingles,espanol=dato.strip().split(":")
        nuevo[ingles]=espanol
    return nuevo
    print(nuevo)
    dicc.close()

    
def buscar(nuevo):
    b=input("ingrese palabra en ingles: ")
    if b in nuevo:
        print(nuevo[i])
    else:
        print("no se encontró")


carga()
nue=listar()
buscar(nue)
