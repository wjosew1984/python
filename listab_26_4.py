#Cargar una lista con 3 elementos enteros, imprimir el mayor y un mensaje si se repite dentro de la lista:

lista=[]
t=0
for x in range(5):
    v = int(input("Ingrese entero: "))
    lista.append(v)
    t=t+lista[x]

k=lista[0]
for x in range(1,len(lista)):
    if lista[x]>k:
        k=lista[x]
print("El mayor elemento es: ",k)
for elemento in lista:#para mostrar qué elemento se repite en una lista se utiliza secuencia "count"
    if lista.count(elemento) > 1:
        print("Se repiten el valor: ",elemento)
