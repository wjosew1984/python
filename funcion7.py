#lo hice con dos "for"

def mayormenor(lista):
    k=lista[0]
    for x in range(len(lista)):
        if lista[x]>k:
            k=lista[x]

    z=lista[0]
    for x in range(len(lista)):
        if lista[x]<z:
            z=lista[x]
    print("El elemento mayor es", k," y el elemento menor es ",z)
        
lista=[]   
for x in range (5):
    v=int(input("Ingrese 5 enteros: "))
    lista.append(v)
    
mayormenor(lista)

