"""
1-Imprimir todos los dígitos decimales, del 0 al 9, utilizando una repetición.
Solución:
for x in range(10):
    print(x)"""

"""#2-Imprimir todos los números entre el 100 y el 199.
#Solución:
for x in range(100,200):
    print(x)"""
"""3-Imprimir los números entre el 5 y el 20, saltando de tres en tres.
Solución:
for x in range(5,20,3): #(inicio, fin, salto)
    print(x)
for x in range(5,20,5): #(inicio, fin, salto)
    print(x)

#4-Requerir al usuario que ingrese un número entero positivo e imprimir todos los números correlativos entre el ingresado por el usuario y uno menos del doble del mismo.
#Solución:
n=int(input("Número: "))
for x in range(n, n*2):
    print(x)

5-Escribir un programa que solicite al usuario una cantidad y luego itere la cantidad de veces dada. En cada iteración, solicitar al usuario que ingrese un número. Al finalizar, mostrar la suma de todos los números ingresados.
Solución:
c=int(input("Cantidad de números: "))
total=0
for variable in range(c):
   numero=int(input("Número: "))
   total+=numero
print("Total de la suma:", total)

6- Solicitar al usuario que ingrese una frase y luego imprimir un listado de las vocales que aparecen en esa frase (sin repetirlas).
Solución:


frase=input("Frase: ")
print("Vocales en la frase:")
for x in "aeiou":
  if x in frase:
    print(x)

7 -Solicitar al usuario que ingrese una frase y luego imprimir la cantidad de vocales que se encuentran en dicha frase.
Solución:

frase=input("Frase: ")
cantidad=0
for x in frase:
    if x in "aeiou":
        cantidad+=1
print("Cantidad de vocales:", cantidad)

8- Escribir un programa que muestre la sumatoria de todos los números entre el 0 y el 100.
Solución:
total=0
for i in range(101):
    total=total+i
print("Sumatoria:", total)

9- Escribir un programa que muestre la sumatoria de todos los múltiplos de 3 encontrados entre el 0 y el 100.
Solución:
total=0
for i in range(101):
    if n % 3 == 0:
        total = total+i
print("Sumatoria de los múltiplos de 3:", total)

10- Dado un número entero positivo, mostrar su factorial. El factorial de un número se obtiene multiplicando todos los números enteros positivos que hay entre el 1 y ese número.
Solución:
numero=int(input("Número:"))
f=1
if numero!=0:
    for i in range(1,numero+1):
        f=f*i
print("Factorial:", f)

11- Crear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci. La sucesión comienza con los números 0 y 1 y, a partir de éstos, cada elemento es la suma de los dos números anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…
Solución:
n1=0
n2=1
print(n1)
print(n2)
for i in range(8):
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3

12- Escribir un programa que permita al usuario ingresar 6 números enteros, que pueden ser positivos o negativos. Al finalizar, mostrar la sumatoria de los números negativos y el promedio de los positivos.
No olvides que no es posible dividir por cero, por lo que es necesario evitar que el programa arroje un error si no se ingresaron números positivos.
Solución:

sumaPositivos=0
cantidadPositivos=0
sumaNegativos=0
for i in range(6):
   nro=int(input("Número: "))
   if nro>0:
       sumaPositivos=sumaPositivos+nro
       cantidadPositivos=cantidadPositivos+1
   else:
       sumaNegativos=sumaNegativos+nro
print("Sumatoria de los negativos: ", sumaNegativos)
if cantidadPositivos!=0:
   print("Promedio de los positivos: ",sumaPositivos/cantidadPositivos)
else:
   print("No se ingresaron números positivos")

13- Un grupo de amigos decide organizar un juego de estrategia, para lo cual forman dos equipos de 6 integrantes cada uno, donde un integrante de cada equipo es el “jefe” y los otros 5 son sus “oficiales”. La regla más importante del juego es que sólo se comunicarán mediante un canal común, por lo que deben buscar la forma de ocultar el contenido de sus mensajes. Uno de los equipos decide utilizar un método antiguo de encriptación llamado “la cifra del césar”, que consiste en correr cada letra del mensaje –considerando la posición de cada una en el alfabeto– una determinada cantidad de lugares. Ejemplo: si el corrimiento es de 2 lugares, la palabra “ATAQUE” se transforma en “CVCSWG”.
Cada día, el “jefe” del equipo debe enviar un mensaje a cada uno de sus oficiales. Escribir un programa que permita encriptar los 5 mensajes. El corrimiento (cantidad de lugares que se correrán las letras) será dado por el usuario antes de comenzar a encriptar. Los 5 mensajes usarán el mismo corrimiento.
Nota: si el alfabeto termina antes de poder correr la cantidad de lugares necesarios, se vuelve a comenzar desde la letra “a”. Ejemplo: la palabra “EXTRA” corrida 3 lugares se convierte en “HAWUD”. Utilizando el alfabeto español, de 27 letras, el siguiente cálculo matemático permite volver a comenzar por el principio una vez que se llegó a la “z”: (índice de la letra a correr+corrimiento)%27
Sólo se encriptarán las letras de los mensajes, dejando al resto de caracteres sin modificación.
Solución:"""
alfabeto="abcdefghijklmnñopqrstuvwxyz"
corrimiento=int(input("Corrimiento: "))
for i in range(5):
    mensaje=input("Mensaje a encriptar: ")
    encriptado=""
    for caracter in mensaje:
        if caracter.lower() in alfabeto:
             indice=alfabeto.find(caracter.lower())
             indice=(indice+corrimiento)%27
             encriptado+=alfabeto[indice]
        else:
             encriptado+=caracter
    print("*** Mensaje encriptado: ", encriptado)