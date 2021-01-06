Listas

Es un contenedor que se usa para almacenar conjuntos de elementos relacionados del mismo o distinto tipo. Son colecciones ordenadas de objetos. A cada elemento se le asigna un índice (posición) comenzando con el cero. 

Creacion
Ej mismo tipo de dato: 
>>> numeros_positivos = [ 1, 6, 8, 12]
>>> nombres = [ "Juan", "Pedro", "Martin", "Constanza"]

Ej distinto tipo de dato: 
>>> info = [ "Ignacio", 2 , -100.5, "*/"]

Vacias: 

lista_vacia = [ ] 
#es útil cuando todavia no conocemos los elementos de la lista al crearla 
print(vacia)
print(type(vacia))

Acceder a los elementos

numeros_positivos = [ 1, 6, 8, 12]
print(numeros_positivos [0])
 
nombres = [ "Juan", "Pedro", "Martin", "Constanza"]
print(nombres[2])
 
vacia = [ ]
print(vacia)
 
info = [ "Ignacio", 2 , -100.5, "*/"]
print(info[ 3])

La consola interactiva nos mostrará la lista completa si indicamos su nombre sin corchetes ni índice: 
>>> nombres = [ "Juan", "Pedro", "Martin", "Constanza"]
>>> nombres


Añadir nuevos elementos una vez creada append() e insert().

sintaxis 
nombre_lista.append(elemento)

numeros_positivos = [ 1, 6, 8, 12]
#print(numeros_positivos [4])
numeros_positivos.append(2)
print(numeros_positivos [4])
 
nombres = [ "Juan", "Pedro", "Martin", "Constanza"]
print(nombres[2])
nombres.append("Julio")
print(nombres[4])
 
vacia = [ ]
print(vacia)
vacia.append(10.2)
print(vacia[0])

Sintaxis
nombre_lista.insert(indice, elemento)

Me permite agregar un elemento en un índice determinado de la lista.

numeros_positivos = [ 1, 6, 8, 12]
numeros_positivos.append(2)
print("Append: ", numeros_positivos [4])
 
numeros_positivos.insert(2 ,-4)
print("Insert:",numeros_positivos [2])
print(números_positivos)
 
nombres = [ "Juan", "Pedro", "Martin", "Constanza"]
print(nombres[2])
nombres.append("Julio")
print("Append:",nombres[4])
 
nombres.insert(5, "Gabriela")
print("Insert:",nombres[5])
print(nombres)
 
vacia = [ ]
print(vacia)
vacia.append(10.2)
print("Append:",vacia[0])
 
vacia.insert(1, -19.6)
print("Insert:",vacia[1])
print(vacia)
Reemplazar los elementos de una lista

Queremos reemplazar el elemento 0 en la lista. Longitud constante.
>>> alumnos = ["Mateo", "Juan", "Pedro"]
>>> alumnos
['Mateo', 'Juan', 'Pedro']
>>> alumnos[0]="Pablo"
>>> alumnos
['Pablo', 'Juan', 'Pedro']
>>>



Remover los elementos de una lista

Sintaxis
del nombre_lista[indice]

>>> info = [ "Ignacio", 2 , -100.5, "*/"]
>>> info
['Ignacio', 2, -100.5, '*/']
>>> del info[0]
>>> info
[2, -100.5, '*/']
>>>
Se achica el len (extensión)

Obtener la cantidad via len()

Sintaxis
len(nombre_lista)

>>> len(info) #3
>>> numeros= [ 1, 2, 3, 4]
>>> len(numeros)
Tambien lo podemos aplicar para saber la cantidad de caracteres de una cadena, ej: 
>>> len("Hola Mundo")
10
>>>

Acceder a los elementos de una lista con len()

Cabe mencionar que cuando queremos acceder al ultimo elemento de la lista no podemos poner números[len(numeros)] porque estaria yéndome por fuera del rango. Entonces como se soluciona, es decir como accedo al valor 4 de la la lista números()?.

>>> vector = ["a", '"', "b", "c"]
>>> vector[1]
>>> vector[0]
>>> vector[len(vector)-1]
>>> vector[len(vector)] #que sucede?
>>> vector[len(vector)-2] #puedo invocar una posición a través de un calculo


Matrices

Es una lista en donde cada elemento contiene una lista. Mas que un concepto matemático nos interesa representar como podemos tener listas dentro de otras listas.

>>> mi_lista = [[3.14, "Hola mundo"], [True, False, -5]]
>>> mi_lista
Ej desde Geany
listaNueva = [[-2, "Hello World"] , ["Juan Perez", True, 66]]
print(listaNueva[0])
print(listaNueva[1])
print("Coordenada 0-0",listaNueva[0][0])
 
#Como hacemos para que nos muestre el valor True
#Como hacemos para que nos muestre el valor "Hello World"

Reemplazamos un valor dentro de una matriz

listaNueva[0][0] = "Nuevo valor"
print(listaNueva)

Ej 2 - Imprimir los elementos de la siguiente matriz (desde el ultimo elemento hasta el primero)
Ejercicio para hacer entre todos.

m1 = [[3.3, 6.1, 4.0], [4.9, 5.7, 6.4]] 


Ej 3 Dadas las siguientes matrices: 

m1= [3.3, 6.1, -4.0]
m2=[5.4, -2.2, 0]

Obtenemos una tercer matriz (m3) que resulte de la suma de sus elementos.

m1= [3.3, 6.1, -4.0]
m2=[5.4, -2, 0]
m3 = [0, 0, 0]
 
m3[0] = m1[0] + m2[0]
m3[1] = m1[1] + m2[1]
m3[2] = m1[2] + m2[2]
 
print(m3)
 
                                                                        Bucles

Son herramientas que me permiten modificar el flujo del programa. Repiten un bloque de codigo en tanto y en cuanto se cumpla una condición.

Bucle “while”

Repite una porción de codigo siempre y cuando una expresion sea verdadera. 

Sintaxis: 
a = 1 
while a < 5: 
    print("Hola mundo")



                                   

Bucle infinito. Se evita cuando la condición se hace Falsa (a) o bien con forzamos la terminación del bucle (b).

Que tendríamos que hacer para que la condición sea falsa en el codigo previo. => incrementador. Hacemos el codigo entre todos.
Palabra reservada break.

a = 1 
while True:
    if a < 5:
        print("Hola Mundo")
        a = a + 1
    else:
        break

Bucle “for”

Repite la ejecución de un bloque de codigo, pero no en base a una condición, sino a un determinado nro de veces. En definitiva ese nro esta vinculado a la cantidad de elementos de la lista, recorrida por el for.

nombres = ["Juan", "Pedro", "Diego", "Pablo"]
for nom in nombres:
    print("Hola Mundo")
#nom es una variable auxiliar que se crea cuando se ejecuta el bucle
#nom va recibiendo los elementos de nombres en el orden en que están guardados
Como hago para que me muestre cada elemento de la lista previa?.


Sino aplico un for, tendría que hacer lo siguiente para todos los elementos de la lista:

print(nombres[0])
print(nombres[1])
print(nombres[2])
print(nombres[3])
Debug bucle FOR

Podemos usar Visual Studio Code o Netbeans con el plugin para Python.

Para eso probamos el siguiente codigo (usando visual studio code debugueamos): F5 start debug, F11 step into

amigos = ["Juan", "Sofia", "Matias", "Josefina"]
 
print("Lista de alumnos: ")
 
for ami in amigos:
    amigo_may = ami.upper()
    print(amigo_may)
 
print("Fin de Programa")


Función range()

Si quisiéramos mostrar los números del 1 al 100 con while como haríamos? Para hacer entre todos.

y con for deberíamos poner todos los nros del 1 al 100

num = [1, 2, 3, 4, ..., 99, 100]
for n in num:
    print(n)
lo cual se vuelve impracticable. Entonces para poder aplicar el for en el ejemplo previo usamos la función range()

num = range(1, 101)
for n in num:
    print(n)
o bien, directamente hacemos

for n in range(1, 101):
    print(n)
Cuando a range() le paso únicamente un numero toma en consideración ese nro como la cantidad de veces que quiero que se ejecute un codigo.

for x in range(5):
    print("Hola Mundo")
la x no la estamos usando para algo, únicamente queremos imprimir 5 veces la frase. Entonces podemos reemplazarla por un guion bajo:

for _ in range(5):
    print("Hola Mundo")

Por que en la siguiente estructura no se muestran los valores del 2 al 4?

a=0
while(a < 5):
    if(a==2):
        continue
    print(a)
    a+=1



                                                                   continue (seguir), break (abortar)

Ambas palabras reservadas se pueden usar para for o para while
primos = [1, 2, 3, 5, 7, 11, 13 ] 
for numero in primos:
    if numero == 3:
        continue
    else:
        print(numero)

primos = [1, 2, 3, 5, 7, 11, 13 ] 
n = 0
 
while(True):
    if n==2:
        break;
    else:
        print(primos[n])
        n+=1

Conversión de cadenas a números 
y viceversa

float a int=>

nroDecimal = 4.5
nroEntero = int(nroDecimal)
print(nroEntero)

str a int =>
cadena_de_texto = "40"
#suma = cadena_de_texto + 1 #arroja un error
 
edad = int(cadena_de_texto)
print(edad)
 
suma_edad = edad + 1
print(suma_edad)

int a str =>

cadena_de_texto = "40"
#suma = cadena_de_texto + 1
 
edad = int(cadena_de_texto)
print(edad)
 
cadena_de_texto = str(edad)
print(type(cadena_de_texto), cadena_de_texto)
 
texto_1 = "Mi edad es: " + cadena_de_texto
print(texto_1)
Dependiendo el uso que queramos darle a los nros serán enteros (operaciones) o String (para mostrar texto y concatenar)

isdecimal() 

isdecimal() retorna True si todos los caracteres de un string son decimales (0 al 9).

Ejercicio 3:  para hacer entre todos

Dado el siguiente codigo que nos indica si podemos votar o no. Hacer una validación con un while por la cual el usuario al ingresar una edad si la edad es numero (isdecimal()) entonces castear ese dato a entero. Sino imprimir por consola que solo se aceptan números.

if edad >=16:
    print("Podes votar")
else:
    print("No podes votar.")
Ejercicio para hacer entre todos: for, conversión, if-elif
Permitir que el usuario ingrese un nro por consola en forma de string.
Transformar ese nro a int.
Generar una lista llamada nro_mes con el nombre literal de cada mes de Enero a Diciembre.
Generar una estructura if-elif por la cual vaya preguntando si el nro_mes (variable que ingreso el usuario) es igual a 1 , igual a 2, …, igual a 11, igual a 12. E imprimir en cada caso el nombre del mes correspondiente. No usar ELSE
BONUS: Hacer lo mismo pero con un for. Para eso crear una lista llamada nros con los nros del 1 al 12 a través de la función range().

Laboratorio, Ejercicios 1, 2.
Proyecto Integrador




