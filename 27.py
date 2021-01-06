lista=[]
pos=0

for x in range (5):
    v=int(input("ingrese un nro entero"))
    lista.append(v)
k=lista[0]
for x in range (1,len(lista)):
    if lista[x]<k:
        k=lista[x]
        pos=x
print ("el menor es: ",k ," la posicion es: ",pos+1)
