"""Repaso clase 1
CODIFICACION
# -*- coding: utf-8 -*-
Lo que hace es indicarle al IDE que interpretara el archivo con una cierta codificación. Esto permite la interpretación de caracteres Unicode que no están en la tablita ASCII (ej caracteres especiales).

Codificacion: 

Es el proceso por el cual cuando escribimos una letra en un ordenador, esa letra se convierte a código ASCII y luego a código binario. Luego otro ordenador lee esa letra y si tienen el mismo sistema de codificación sabe que letra es, la convierte a código binario y la reconoce como la misma letra que estaba en el otro ordenador. 
 
Cabe aclarar que esta línea es un tema de Python 2. En Python 3 la codificación por defecto es UTF-8. Solo cuando queremos desviarnos de esta codificación debemos colocar esa línea en Python3. Sobre todo cuando tenemos en un mismo proyecto códigos con diversa codificación.

Referencia:
https://stackoverflow.com/questions/4872007/where-does-this-come-from-coding-utf-8 

Calcular Raiz Cuadrada (alternativa)

import math
 
#obtenemos la raiz cuadrada
"""
numero = 25
raiz_cuadrada = math.sqrt(numero)
print("La raíz cuadrada de {} es {}".format(numero, raiz_cuadrada))
 
#obtenemos la potencia
numero = 5
elevado = math.pow(5, 3)
print("{} elevado a la potencia 3 es {}".format(numero, elevado))



Tipo de Datos

Los tipos de dato permiten clasificar la información que contiene una variable. 

Numeros Enteros. 
Numeros de coma flotante (racionales). 
Cadenas de caracteres.
Booleanos. 

Ej: 
Pi = 3.14
apagado = True (Python es case-sensitive, con lo cual True!=TRUE)

Instrucción Type 
Permite saber el tipo de dato. type()

Ejercicio para hacer entre todos (a)
Si con type(a) sabemos que podemos obtener el tipo de dato de la variable. Si a fuera 5 como hacemos para que se muestre el tipo de dato con Geany?.

          Diferencias entre los Tipos de Datos

El tipo de dato influirá sobre las operaciones que puedo realizar.

a = True        #valor logico que puede ser V o F
print(type(a))
 
b = 3.14        #coma o punto flotante (nros racionales)
print(type(b))
 
c = "Hola Mundo"  #cadena de caracteres o string (texto)
print(type(c))
 
a = 2             #entero
print(type(a))
Operaciones aritméticas
Con números enteros

print(7 * 5 + 1)
print ( 7 / 5)
#Operador ** (Cuadrado, potenciacion)
print('Operador "**"')
a = 3
b = 3 **2
print(b)
#Tambien podemos usar paréntesis
print(7 + 5 * 3)
print((7 + 5) * 3)
 

Ejercicio para hacer entre todos (b)
Como hacemos para ver el tipo de dato que se obtiene de la división previa 7 / 5?

Operaciones aritméticas
Con números flotantes

pi = 3.14
 
#Operador -
print('Operador "-"')
resultado = pi - pi
 
print(resultado)
print(type(resultado))
 
#Operador /
a = 5
print('Operador "/"')
print(a / pi)

Operadores de comparación 

== (igualdad),      
!= (desigualdad),   
> (mayor), 
>= (mayor o igual), 
< (menor) 
<= (menor o igual).

El resultado será un boolean (true or false)

Vamos a la consola interactiva >>>

7 > 5 
7 <= 5 
7 != 5 
7 == 5 
5 >= 7 
5 < 7 
Los operadores >, >=, < y <= solo pueden aplicarse para nros entero o coma flotante. Mientras que == y != permiten comparar los cuatro tipo de datos.

Geany
print("Hola" == "mundo")
 
print(3.14 != True)
Desde Consola interactiva podemos indicar un valor True en forma de expresion.
edad = 30
edad >=16    #para saber si una persona puede votar o no.
Puede_votar = edad >=16   #la expresion edad >=16 indica Verdadero. 
                          #Es lo mismo que poner True 
                          
Diferencia entre = y ==
Asignacion vs igualdad(comparación). = asignamos el valor a una variable, == chequeamos T o F. Para esto ultimo no se puede usar = sino pisaría el valor de la variable. Por eso usamos ==.


Operaciones Lógicas

Nos permiten hacer comparaciones mas complejas

and (conjunción) “y”

Como hago para decir si un numero es mayor a 4 y menor a 20?. Utilizamos la variable a.

or (disyunción) “o”        

Como hago para decir si un nro es mayor a 4 o menor igual a cero?.

not (negación): invierte el valor logico de un booleano

a = not True
b = a
print(b)
 
pi = 3.14
print(not pi == 3.14)
 

Dados:
>>>a = 5 
>>> pi = 3.14 
Que les parece que darán las siguientes comparaciones?.
>>> not pi == 3.14 and a == 1 or a == 10 


Tabla de Verdad

Dados los siguientes valores:
a = True
b = False
c = not a
d = a

Que resultado obtendremos de la siguiente comparación?:
((a and b) or (c or (d and not a)))      (hacer en Geany)


Estructuras Condicionales 
 
Permiten cambiar la forma en el flujo del codigo.

Estructura IF
Evalua si una condición es V o F. Si es V ejecuta las sentencias después del IF. Si es F continua con el programa.




a = 12
if a < 22:
      print("a es menor que 22.")
      print("se cumplio la condicion")
print("Hola mundo")
Sangria: Indica a Python cual es el bloque o linea/s de codigo que se ejecutara cuando se cumple la condición, es decir es verdadera. En este caso ingresa al IF.
Indentacion. El IF debe estar indentado. En Geany se aplica automáticamente luego de colocar “:” y enter. 

En el ej previo la linea print(“Hola mundo”) esta por fuera de la estructura IF. Se va a ejecutar si o si.

Ejercicio para hacer entre todos(C): 
Definir una variable a igual al nro pi.
Crear una estructura IF.
Si el cuadrado de a es mayor a 7 entonces imprimir “El cuadrado de “a” es mayor a 7”.
Crear otro IF con la siguiente condición. Si a es mayor a 7 entonces imprimir “a es mayor a 7”. 
FIN de los bloques IF







Estructura IF-ELSE

Se utiliza para evitar poner dos if o tener que poner if not condición. Es optativo el uso de paréntesis.


a = 12 
if a > 10: 
    print("a es mayor que 10.") 
else: 
    print("a es menor o igual que 10.")
 
IF y ELSE deben tener misma sangria. Sino no funciona.

El ejemplo anterior, estructura IF-ELSE es similar a la siguiente
a = 2
if a > 10:
    print("a es mayor que 10.")
if not a > 10:
    print("a es menor que 10.")
Y a la siguiente 
a = 2
if a > 10:
    print("a es mayor que 10.")
if not a <= 10:
    print("a es menor o igual que 10.")

Condicionales Multiples IF – ELIF -ELSE


ELIF: Nos permite agregar mas de una condición en el mismo condicional. Es decir, tenemos un condicional con multiples condicionales.



a = 5
if a == 1:
 print("a es 1.")
elif a == 2:
 print("a es 2.")
elif a > 2 and a < 10:
 print("a es mayor que 2 y menor que 10.")
else:
 print("a es mayor o igual que 10.")

Condicionales Anidados IF (IF-ELSE) ELSE: (IF-ELSE)

Ponemos condicionales dentro de condicionales.

edad = int(input("Ingrese su edad por favor")
 
if edad >=16:
    if edad >=65:
        print("Votacion opcional.")
    else:
        print("Puede votar")
 
else:
    if edad <= 15:
        print("Sos demasiado joven")
    else:
        print("No puede votar.")

Comentarios #

Lineas dentro de un archivo .py que Python ignorara por completo. 
A nivel de codigo.
Varias líneas => CTROL + E

Entrada de datos

Es la operación inversa a print(). El usuario ingresa información por consola y se puede guardar en una variable. 

Instrucción input(): siempre guarda una cadena.

nombre = input("Escribe tu nombre: ")
print(nombre)

Si el usuario ingreso un numero se puede realizar la conversión, ej: 
codPost = int(input("Ingrese su codigo postal: "))
        
print(codPost)
print("Codigo Postal: ",codPost)
“,” - “+” print()

nombre = "Juan"
print("Hola"+nombre)
print("Hola",nombre) #la coma se traduce en un espacio 



Ejercicio para realizar entre todos (D):

Pedirle al usuario que ingrese su nombre y guardar el string en una variable “nombre”.
Si el nombre == “tu nombre” entonces concatenar el nombre que puso el usuario con la frase “ es tu nombre”.
Sino concatenar el nombre que puso el usuario con la frase “ no es tu nombre”.
Ejercicios

1) Implementar el siguiente algoritmo teniendo en cuenta que el discriminante ─el interior de la raíz─ puede ser un número negativo o cero. 
En ese caso el programa debe imprimir que no hay solución posible (discriminante negativo) o bien mostrar la única solución posible (discriminante cero). 


Unica solución posible
a = 1
b = 2 
c = 1
No hay solución posible
a = 10
b = 2
c = 1
Dos raíces
a = 1
b = 4
c = 2

2) Insertar un número por consola e indicar si el mismo es o no par(con módulo) 

Input - int

If print(es par) – else print (es impar)


3) Calculadora: Ingresar dos números y un operador(+,-,*,/) e imprimir el resultado de la siguiente manera: Resultado: 3 + 4 = 7 elif Ingresar por consola número de mes e imprimir nombre de mes correspondiente. (Tarea)

4) Crea una variable numérica y si esta entre 0 y 10, mostrar un mensaje indicándolo. 

5) Añadir al anterior ejercicio, que si esta entre 11 y 20, muestre otro mensaje diferente y si esta entre 21 y 30 otro mensaje. Sino esta en ninguno de los rangos que muestre “No esta en este rango”. (Tarea)


Realizar los ejercicios del laboratorio.

