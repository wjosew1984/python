#FUNCIONES

#Concepto

#"Una función es una porción o bloque de código reutilizable que se encarga de realizar una determinada tarea."

#Por ejemplo si queremos ejecutar el siguiente código:

print("¡Calculos!")
print("Desde Python.")
 
a = 11
b = 54
c = a * b
print(c)
 
print("¡Calculos!")
print("Desde Python.")
#podemos aplicar funciones para aplicar las líneas que precisemos en un determinado momento de la ejecución de nuestro programa.

#Definicion   

#La creamos con la palabra reservada def. 

def mi_funcion():
    print("¡Calculos!")
    print("Desde Python.")
 
mi_funcion()
a = 11
b = 54
c = a * b
print(c)
 
mi_funcion()

#Una vez creada y definida se llama o invoca (Ejecucion de la Funcion)

#Argumentos 
#Indicamos en paréntesis la o las variables que serán utilizadas en la función en un momento determinado de la ejecución. En este caso, lista (definida en la función) será reemplazada por cada lista enviada como argumento.

colores = ["Rojo", "Azul", "Violeta", "Blanco" ]
pulgadas = [16.5, 57.8, -3.2, 1]
 
#Si queremos imprimir el contenido de cada lista como seria?
print("Sin Funcion: ")
 
print("\nColores: ")
for col in colores:
    print(col)
    
print("\nPulgadas: ")
for pul in pulgadas:
    print(pul)
    
#Como podemos abreviar la impresion, dado que se repite la misma logica
 
def impresion(lista):
    for elemento in lista:
        print(elemento)
        
#entonces una vez definida la funcion la podemos utilizar donde precisemos
print("\nAplicamos Funcion: ")
print("\nColores: ")
impresion(colores)          
 
print("\nPulgadas: ")
impresion(pulgadas)          
 
print("\nIncluso podemos pasar una lista explicitamente:")
impresion([1, 2, 3, 4, 5, 6])    

#Multiples argumentos 

#Ejercicio para hacer entre todos (a)

#Definir una funcion llamada potencia por la cual le pasamos dos números y en 1 sola línea tiene que mostrar “La potencia del 1er numero es: resultado”.
#Donde 1er numero es: a 
#Y resultado es el resultado de la potencia.

#Luego llamar a la función pasandole dos argumentos. 
#Hint: Para colocar mas de un argumento los mismos se separan en comas.
#En la definición de la función agregar también los textos: 
#“La base es: “ 
#“El exponente es: “

#Orden de los argumentos

#Llamada a la función => debe coincidir el orden a como estan ordenados en la definicion. Dentro de la función se pueden usar en cualquier orden.

#Pasar argumentos en un orden diferente: 

potencia(b = 2, a = 3)    #indicamos el nombre en forma explicita.

Valor de retorno (return)

Ejercicio para hacer entre todos (b)
#Como hacemos para que en el ejercicio anterior en lugar de mostrar el resultado de la potenciación, que muestre solo la base y el exponente pero que me devuelva el resultado. 
#Una vez que lo devuelva que se muestre desde la llamada a la función.

Tipo de dato => cualquiera de los 4 tipos + Listas.

#Ej

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
#Ejercicio para hacer entre todos (c)

#¿Cómo hacemos para que la lista que obtuve en el ejercicio previo además de imprimirla me devuelva el ultimo valor?. 
#           Crear una función que realice tal efecto. Usamos len().
#Y si queremos traer el ultimo elemento de la lista usando las dos funciones simultáneamente como haríamos?

#Ejercicio de laboratorio: 

Imprimir matriz con una función

Crear una función que tome como argumento una matriz, de cualquier dimensión, e imprima cada uno de sus números en una línea diferente. Por ejemplo, el siguiente código:

m1 = [[3.3, 6.1, 4.0], [4.9, 5.7, 6.4]]
imprimir_matriz(m1)

debe imprimir:

3.3
6.1
4.0
4.9
5.7
6.4


Ejercicio de laboratorio: Sumar números con una función 

Crear una función que tome como argumento una lista (considerando que siempre contendrá números enteros y de coma flotante) y retorne la suma de todos sus elementos. Por ejemplo, el siguiente código:

print(sumar([1, 2, 3, 4, 5]))

debe imprimir: 15 (1 + 2+ 3+ 4+ 5)


Ejercicio (Video) para devolver mas de un valor (Lista) ***

Definir una función a la cual le paso una lista, llamada min_max. La función debe obtener el mínimo y el máximo de la lista, como hacemos para devolver los dos valores si solo podemos devolver un valor por return?


-Calcular las raíces de una ecuación de segundo grado (por ejemplo, raices(a, b, c) y que el resultado sea una lista [x1, x2]).

Rango 
Definir una función llamada rango la cual cumpla la misma función que range(desde, hasta, intervalo). 
Donde vaya apendeando elementos siempre y cuando desde sea menor a hasta. Y finalmente que devuelva la lista de números de ese rango.

PRINT VS RETURN en funciones
FUNCIONES => lógica
PRINT => salida al usuario layout.


Dentro de Colecciones podemos tener listas y diccionarios.




Diccionarios
Los diccionarios son colecciones, al igual que las listas, pero sus elementos (o valores ) no están ordenados ni asociados a un índice, sino a una clave . Sus miembros son pares de clave-valor. Nos permiten albergar información mas compleja.
Por ejemplo:

jugadores = {"nombre": "Gabriel", "Nro: ": 9}

Los valores de un diccionario pueden ser de cualquier tipo de dato, incluidos otros diccionarios y listas.  Las claves tienen algunas restricciones por ejemplo no pueden repetirse y no pueden ser una lista. Pueden ser un nro o una cadena.

¿Cómo creen que podemos acceder a los valores del diccionario?


Podemos crear también nuevos pares clave-valor:


jugadores["apellido"] = "Batistuta"
 
print(jugadores["apellido"])
Con un bucle for sobre el diccionario tenemos acceso a cada una de sus claves, por ejemplo:


jugadores = {"nombre": "Gabriel", "Nro: ": 9}
for jug in jugadores:
    print(jug)
 
jugadores["apellido"] = "Batistuta"
 
for jug in jugadores:
    print(jug)
Si queremos imprimir las claves y los valores como haríamos?.

La clave en los diccionarios es equivalente a los índices en las listas. Cuando creo diccionarios es como si estuviera creando nuevos tipos de datos.

Proyecto Integrador



Codigo Proyecto integrador Clase 3

#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
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
