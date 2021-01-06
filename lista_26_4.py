#Crear y cargar una lista con 5 enteros por teclado, mostrar el menor valor de la lista y la posición doónde se encuentra:

lista=[]
t=0
for x in range(5):
    v = int(input("Ingrese entero: "))
    lista.append(v)
    t=t+lista[x]
print(f"La lista contiene {lista} y {[len(lista)]} elementos")

k=lista[0]#nombro k al 1er elemento de la lista
for x in range(1,len(lista)):#compara con k del 1 en adelante con el resto de la lista(len)
    if lista[x]<k:#acá es donde pasa si es mayor o menor en la lista
        k=lista[x]#guarda en k el elemento mayor o menor
print("El elemento menor es: ",k, "Se encuentra en la posición:",(lista.index(k)))





