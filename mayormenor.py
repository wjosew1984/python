lista=[]
for x in range (5):
    v=int(input("ingrese valor: "))
    lista.append(v)
lista.sort(reverse=True)
print (lista[0])
print (lista[len(lista)-1])
