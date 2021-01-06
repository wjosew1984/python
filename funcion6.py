def suma(lista):
    tot=0
    for x in range(len(lista)):
        tot=tot+lista[x]
    return tot

def mayor(lista):
    k=lista[0]
    for x in range(len(lista)):
        if lista[x]>k:
            k=lista[x]
    return k

def menor(lista):
    z=lista[0]
    for x in range(len(lista)):
        if lista[x]<z:
            z=lista[x]
    return z

lista=[1,5,9,12,36]

s=suma(lista)
print("La suma total es: ",s)

ma=mayor(lista)
print("El elemento mayor es: ",ma)

me=menor(lista)
print("El elemento menos es: ",me)
