print("¡Calculos!")
print("Desde Python.")
 
a = 11
b = 54
c = a * b
print(c)
 
print("¡Calculos!")
print("Desde Python.")

def mi_funcion():
    print("¡Calculos!")
    print("Desde Python.")
 
mi_funcion()
a = 11
b = 54
c = a * b
print(c)
 
mi_funcion()

colores = ["Rojo", "Azul", "Violeta", "Blanco" ]
pulgadas = [16.5, 57.8, -3.2, 1]

print("Sin Funcion: ")
 
print("\nColores: ")
for col in colores:
    print(col)
    
print("\nPulgadas: ")
for pul in pulgadas:
    print(pul)
 
def impresion(lista):
    for elemento in lista:
        print(elemento)

print("\nAplicamos Funcion: ")
print("\nColores: ")
impresion(colores)          
 
print("\nPulgadas: ")
impresion(pulgadas)          
 
print("\nIncluso podemos pasar una lista explicitamente:")
impresion([1, 2, 3, 4, 5, 6]) 

#potencia(b = 2, a = 3)    indicamos el nombre en forma explicita.

def rango(desde, hasta):
    numeros = []
    while desde <= hasta:
        numeros.append(desde)
        desde = desde + 1
    return numeros
 
des = int(input("Ingrese el rango desde: "))
has = int(input("Ingrese el rango hasta: "))
 
lista = rango(des, has)
print(lista)

m1 = [[3.3, 6.1, 4.0], [4.9, 5.7, 6.4]]
#imprimir_matriz(m1)

# debe imprimir:

3.3
6.1
4.0
4.9
5.7
6.4

import os
 
alumnos = []
aux = 0
 
while(True):
    print("\nIngrese el nro de la operacion que desea ejecutar: ")
    print("1- Ver la lista de alumnos.")
    print("2- Añadir un alumno a la lista.")
    print("3- Salir.")
    valor = int(input(""))
    os.system("cls")
    
    if(valor==1):
        if(aux==1):
            print("Lista de Alumnos: ")
            for alumno in alumnos:
                nomb = alumno[0]
                cur = alumno[1]
                print(nomb + " - ", str(cur)+" cursos")
        else:
            print("No hay alumnos en la lista.")
    elif(valor ==2):
        
        nombre = input("Ingrese el nombre de un alumno: ")
        cant_cursos = int(input("Cantidad de cursos inscriptos: "))
        alum = [ nombre , cant_cursos ]
        alumnos.append(alum)
        aux=1
        print("¡El alumno fue añadido a la lista!")
    elif(valor == 3):
        os.system("cls")
        print("¡Gracias por utilizar el programa!")
        break
    else:
        os.system("cls")
        print("La opcion ingresada no es correcta, vuelva a intentarlo")
