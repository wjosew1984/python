
def entradas():
    li=[]
    for x in range (5):
        v=int(input("Ingrese 5 enteros: "))
        lista.append(v)
    return li

def mayores(lista):
    for x in range(5):
        if lista[x]>10:
           print (lista[x])
        
lista=entradas(li)
mayores(lista)
