def carga():
    responde=input("desea cargar?(si/no)")
    dic={}
    while responde=="si":
        ing=str(input("ingrese palabra en ingles: "))
        esp=str(input("ingrese su trad al español: "))
        dic[ing]=esp
        responde=input("desea cargar?(si/no)"):    
    return dic

def imprime(dic):
    for ing in dic:
        print(ing,dic[esp])
        
def buscador(dic):
    palabra=input("que palabra desea traducir: ")
    if palabra in dic:
        print(dic[esp])

diccionario=carga()
imprime(diccionario)
buscador(diccionario)
                  
                 
                         
                     
                 
                 
