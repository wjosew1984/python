#ejercicio 1
"""suma = 0
for n in range(0,5):
    numero = int(input("Introduce un numero"))
    suma = suma + numero
print("La suma es", suma)

suma = 0
for f in range(0,5):
    numero = int(input("Ingrese un numero"))
    suma = suma + numero
    print(suma)
"""
#jose = ("Hola Mundo!")
#print("Hola Mundo!")
#saludo = ("Hola, Mundo")

#print(saludo)
"""
name = input("Introduce tu nombre: ")
print("¡Hola " + name + "!")

namo = "Jose Luis"
edad = "36"
profesion = "tester"

datos = (namo , edad , profesion)
print(datos)

Ejercicio 1
Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:

Mostrar una suma de los dos números
Mostrar una resta de los dos números (el primero menos el segundo)
Mostrar una multiplicación de los dos números
En caso de introducir una opción inválida, el programa informará de que no es correcta.

Solución
"""
n1 = float(input("Introduce un número: ") )
n2 = float(input("Introduce otro número: ") )
opcion = 0
n1(type)
print(n1(type))

print("""
¿Qué quieres hacer?
1) Sumar los dos números
2) Restar los dos números
3) Multiplicar los dos números
""")

opcion = int(input("Introduce un número: ") )     

if opcion == 1:
    print("La suma de",n1,"+",n2,"es",n1+n2)
elif opcion == 2:
    print("La resta de",n1,"-",n2,"es",n1-n2)
elif opcion == 3:
    print("El producto de",n1,"*",n2,"es",n1*n2)
else:
    print("Opción incorrecta")
"""Resultado
Ejercicio 2
Realiza un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, debe repetise el proceso hasta que lo introduzca correctamente.

Solución

numero = 0
while numero % 2 == 0:  # Mientras sea par repetimos el proceso
    numero = int(input("Introduce un número impar: ") )
Resultado
Ejercicio 3
Realiza un programa que sume todos los números enteros pares desde el 0 hasta el 100.

Sugerencia

Puedes utilizar la funciones sum() y range() para hacerlo más fácil.
El tercer parámetro en la función range(inicio, fin, salto) indica un salto de números, pruébalo.

Solución

# Primera forma con función sum()
suma = sum( range(0, 101, 2) )
print(suma)

# Segunda forma con bucles
num = 0
suma = 0

while num <= 100:
    if num % 2 == 0:
        suma += num
    num += 1

print(suma)
Resultado
Ejercicio 4
Realiza un programa que pida al usuario cuantos números quiere introducir. Luego lee todos los números y realiza una media aritmética.

Solución

suma = 0
numeros = int(input("¿Cuántos números quieres introducir? ") )
for x in range(numeros):
    suma += float(input("Introduce un número: ") )
print("Se han introducido", numeros, "números que en total han sumado", 
        suma, "y la media es", suma/numeros)
Resultado
Ejercicio 5
Realiza un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea correcto se repita el proceso. Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:

Concepto útil

La sintaxis [valor] in [lista] permite comprobar si un valor se encuentra en una lista (devuelve True o False).

Ejercicio

numeros = [1, 3, 6, 9]

# Completa el ejercicio aquí
Solución
Resultado
Ejercicio 6
Utilizando la función range() y la conversión a listas genera las siguientes listas dinámicamente:

Todos los números del 0 al 10 [0, 1, 2, ..., 10]
Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]
Concepto útil

Se pueden generar saltos en el range() estableciendo su tercer parámetro range(inicio, fin, salto), experimenta.

Solución

print(list(range(0, 11)))
print(list(range(-10, 1)))
print(list(range(0, 21, 2)))
print(list(range(-19, 0, 2)))
print(list(range(0, 51, 5)))
Resultado
Ejercicio 7
Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, pero no debe repetirse ningún elemento en la nueva lista:

Ejercicio

lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']

# Completa el ejercicio aquí
"""