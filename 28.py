lista=[]
for x in range (5):
    v=int(input("ingrese un nro entero"))
    lista.append(v)

lista.sort()
print (lista[len(lista)-1])

k=lista[0]
for x in range (1,len(lista)):
    if lista[x]>k:
        k=lista[x]
for x in range(5):
    if (lista[len(lista)])==lista[x]:
        print ("hay dos valores iguales")
