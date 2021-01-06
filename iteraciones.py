"""
Iteraciones
Iterar significa realizar una acción varias veces. Cada vez que se repite se denomina iteración.

Sentencia while (mientras)
Se basa en repetir un bloque a partir de evaluar una condición lógica, siempre que ésta sea True. Queda en las manos del programador decidir el momento en que la condición cambie a False para hacer que el While finalice.

Código
"""
c = 0
while c <= 5:
    c+=1
    print("c vale", c)
"""
Resultado
Uso de else en while
Se encadena al While para ejecutar un bloque de código una vez la condición ya no devuelve True (normalmente al final):

Código
Copiado al portapapeles
"""
c = 0
while c <= 5:
    c+=1
    print("c vale", c)
else:
    print("Se ha completado toda la iteración y c vale", c)
"""
Resultado
Instrucción break
Sirve para "romper" la ejecución del While en cualquier momento. No se ejecutará el Else, ya que éste sólo se llama al finalizar la iteración.:

Código
"""
c = 0
while c <= 5:
    c+=1
    if (c==4):
        print("Rompemos el bucle cuando c vale", c)
        break
    print("c vale",c)
else:
    print("Se ha completado toda la iteración y c vale", c)
"""
Resultado
Instrucción continue
Sirve para "saltarse" la iteración actual sin romper el bucle.

Código
"""
c = 0
while c <= 5:
    c+=1
    if c==3 or c==4:
        # print("Continuamos con la siguiente iteración", c)
        continue
    print("c vale",c)
else:
    print("Se ha completado toda la iteración y c vale", c)
"""
Resultado
Ejemplo menú interactivo
Código
"""
print("Bienvenido al menú interactivo")
while(True):
    print("""¿Qué quieres hacer? Escribe una opción
    1) Saludar
    2) Sumar dos números
    3) Salir""")
    opcion = input()
    if opcion == '1':
        print("Hola, espero que te lo estés pasando bien")
    elif opcion == '2':
        n1 = float(input("Introduce el primer número: "))
        n2 = float(input("Introduce el segundo número: "))
        print("El resultado de la suma es: ",n1+n2)
    elif opcion =='3':
        print("¡Hasta luego! Ha sido un placer ayudarte")
        break
    else:
        print("Comando desconocido, vuelve a intentarlo")
"""
Resultado
Sentencia for (para)
for con listas
Para ilustrar la utilidad de esta sentencia vamos a empezar mostrando como recorrer los elementos de una lista utilizando While:

Código
"""
numeros = [1,2,3,4,5,6,7,8,9,10]
indice = 0
while indice < len(numeros):
    print(numeros[indice])
    indice+=1
"""
Resultado
Lo mismo utilizando el For:

Código
"""
for numero in numeros:  # Para [variable] en [lista]
    print(numero)
"""
Resultado
¿Mucho más fácil no?

Para asignar un nuevo valor a los elementos de una lista mientras la recorremos, podríamos intentar asignar al número el nuevo valor:

Código
"""
for numero in numeros:
    numero *= 10   
numeros
"""
Resultado
Sin embargo, esto no funciona. La forma correcta de hacerlo es haciendo referencia al índice de la lista en lugar de la variable:

Código
"""
indice = 0
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros:
    numeros[indice] *= 10
    indice+=1
numeros
"""
Resultado
Podemos utilizar la función enumerate() para conseguir el índice y el valor en cada iteración fácilmente:

Código
"""
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for indice,numero in enumerate(numeros):
    numeros[indice] *= 10
numeros
"""
Resultado
for con cadenas
Funciona exactamente igual que con las listas, pero con caracteres en lugar de elementos:

Código
"""
cadena = "Hola amigos"
for caracter in cadena:
    print(caracter)
"""
Resultado
Pero debemos recordar que las cadenas son inmutables:

Código
"""
for i, c in enumerate(cadena):
    cadena[i] = "*"
"""
Resultado
Sin embargo siempre podemos generar una nueva cadena:

Código
"""
cadena = "Hola amigos"
cadena2 = ""
for caracter in cadena:
    cadena2 += caracter * 2 
"""
Resultado
La función range()
Sirve para generar una lista de números que podemos recorrer fácilmente, pero no ocupa memoria porque se interpreta sobre la marcha:

Código
"""
for i in range(10):
    print(i)
"""Resultado
Esta función devuelve un generador, una estructura manejada en tiempo de ejecución:

Código

range(10)
Resultado
Si queremos conseguir la lista literal podemos transformar el range a una lista:

Código

list(range(10))
"""