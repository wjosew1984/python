Introducción a la programación:
Un poco de Historia e introducción al Lenguaje
Surge en los años 90. Creado por el Holandes Guido van Rossum. 
Lenguaje alto nivel: Cercano al ser humano. 
Lenguaje de bajo nivel: Cercano a codigo binario. 1 y ceros.
Python esta orientado a objetos tal como Java. Lo único que mas sencillo. La POO es una filosofía en la resolución de problemas. Hay otros tipos de Programacion (funcional, recursiva). Python es multi-paradigma. Tambien es multi-plataforma (se puede correr en Windows, Linux, Unix, y otras). Puede ser multi-plataforma por que es un lenguaje interpretado.
El interprete es un programa que me permite interpretar el lenguaje de programación y poder ser ejecutado en el sistema operativo.
Python se usa: 
Analisis de datos. 
Seguridad. 
Automatizacion de Procesos. Robotizacion. Rutinas diarias.
Programacion Web. 
Y es de tipado dinamico (lo veremos en variables).
La ultima clase haremos una aplicación de escritorio con un entorno grafico.

Que es programar?
Es decirle a una computadora lo que tiene que hacer. El programador es el que diseña esas instrucciones según las reglas de un lenguaje de programación en particular. Y esas instrucciones serán el programa o aplicación (codigo).
Entonces programar puede pensarse como un proceso de comunicación, donde hay un emisor y receptor. Y el medio de comunicación es el lenguaje.

Programa o Aplicación: Mensaje codificado según las reglas de un lenguaje de programación.
Codigo Maquina. => precisamos un Traductor: convierte instrucciones escritas a codigo maquina. En donde Python (programa) es el interprete.

El interprete es lo que nos referimos cuando decimos instalar Python. Python el programa es el interprete que traduce el lenguaje de Python en lenguaje de maquina.
El dispositivo programable por su parte interpreta codigo binario (ceros y unos).
Caracteristica de Python: Sintaxis sencilla y clara.
Ejemplo de aplicaciones: Dispositivos mobiles, Web (Python), de escritorio (Python), de consola (Python).
Tipos de Aplicaciones que nos enfocaremos: De consola, y de escritorio (contiene una interfaz grafica).


Preparación del entorno.
Vemos la guía de instalación de Python. Version 2 de Python, caduco en el 2018 y con soporte hasta 2020. Las bibliotecas que estaban pensadas para Python 2 no van a tener actualizaciones. Los scripts de Python 2 no van a poder correr en Python 3.

Al Instalar Python recordar ubicar el path en una ruta amigable, ej c:/. 
Editor de codigo: IDE. => nos permiten programar. => Ej: Geany, block de notas

Extensión .py => codigo fuente.

Expresiones

Es una porción de codigo que ejecuta una operación o tarea determinada. Y obtiene un resultado.

Operaciones aritméticas: son ejemplo de expresion. => 7 + 5, se ejecuto y obtiene un resultado. 
Print(“Hola Mundo”): también es una expresion.

Sintaxis: orden y la relación de los términos de un lenguaje necesarios para que una instrucción sea comprendida.

Para la suma la sintaxis es:

7 + 5  (colocamos esta sintaxis en Geany)

Por que no muestra nada? Como les parece que hacemos para que muestre el resultado?.

“ “ : interpreta de forma literal y no como codigo de Python.
Por eso cuando ingresamos print(“7 + 5”) lo muestra literalmente

Entonces volviendo a nuestra expresion 7 + 5. 
Expresion: Es un fragmento de codigo que retorna un resultado.

Retornar significa reemplazar en ese fragmento de codigo por su resultado.
Entonces print ( 7 + 5) es igual a print (12). Primero resuelve la expresion y en el lugar donde esta escrita la expresion reemplaza con el resultado.
print ( 7 + 5 + 10): resuelve de izquierda a derecha. Primero 7 + 5 y luego 12 + 10.
El termino “reemplazar” se usa a fines didácticos para comprender el concepto de expresion. 


Variables

Que es una variable?
Es un lugar en memoria que el interprete crea para guardar un determinado dato. 

variable = 10
variable

Sintaxis: 
nombre_variable = expresion
(minúsculas sin espacios)

a = 7 + 5

Creacion de una variable => 1. Definicion y 2. Asignacion

Ej: 
a = 7 + 5
print (a)

Creo otras expresiones en base a la variable previa

a = 7 + 5
print (a + 10)

Y también puedo crear otras variables.
a = 7 + 5
b = a  + 10
print(b)

Las variables son en si mismas expresiones. Esto significa que Python reemplazara a por 12 en toda ocurrencia de a. Y para una variable saludo que contiene el valor “Hola mundo”.

Tipo de datos: En otros lenguajes debemos definir el tipo de dato. 
Tipado Dinámico:  No hace falta declarar el tipo de dato en Python. Se pueden sobreescribir los valores.
Ej: a= 10;  a = 10.5; a=’hola’



Consola Interactiva “>>>”

No sirve para hacer programas, simplemente es una interacción (charla) con el interprete.
Nos permite escribir codigo Python sin necesidad de guardarlo en un archivo .py. Es una forma de probar codigo Python y probarlo rápidamente.

Windows + R => Python

7 + 7: muestra el resultado.
String: print(“hola mundo”)

Modulo: Explicamos Resto. 
%
Ej: 10%2
       9%2

type(a)


IDE - GEANY



Seteo 1 Espacios => Documento – Tipo de Sangria – Espacios
Seteo 2 espacios => Editar – Preferencias – Editor – Sangria – Seleccionar “Espacios”
Este seteo evita que luego tengamos problemas en algun programa cuando se mezclen espacios y tabulaciones.

Primer Programa “Hola Mundo”
Con Geany.
En general es el 1er programa que se ejecuta cuando aprendemos programación.
Guardamos el archivo en nuestra carpeta de trabajo, borramos el codigo previo y escribimos: 

#!/usr/bin/env python     
# -*- coding: utf-8 -*- 

#!/usr/bin/env Python (llama al interprete en Linux) 
buscará el ejecutable del comando python de acuerdo a las rutas definidas en el $PATH de tu entorno (cuando se trata de Unix o Linux). Para Windows no aplica. 
Los caracteres #! se los conoce como shebang (Unix). 
La segunda linea se refiere a la codificación en español de ciertos caracteres especiales.

print("Hola mundo")

Ejecutar o F5

Lo guardamos como hola.py.

Consola: Windows + R => CMD

Terminal como aplicacion. Vemos la diferencia entre movernos con el explorador y con la consola. Y también la diferencia en como ejecutamos desde el explorador y desde la consola.

dir: me permite ver el contenido de una carpeta.

cd (change directory) vamos al archivo donde se encuentra nuestra aplicación.

Acceder a una ruta que contiene espacios => con comillas. Ej cd “c:\Program Files (x86)\Geany”

ping: programa para saber si una dirección de ip o dominio esta corriendo.
Solo hay 2 operaciones (ingresar instrucciones, output de mensajes en consecuencia a las instrucciones) => ping www.mercadolibre.com.ar

Probamos ejecutar el archivo hola.py desde la ruta
C:\Users\lrlopez\Desktop\PYTHON\CLASE 1>
con el cmd.
python hola.py


Algunas consideraciones 

Doble click del programa desde el origen. Y la diferencia que hay corriéndolo desde un IDE.

Script: Conjunto de instrucciones guardadas en un archivo con extensión .py.

Formas de ejecutar un script en Python: 1. Desde el IDE. 2. Con el archivo 3. Desde la consola o terminal.

Al finalizar la linea no es necesario poner “;” como otros lenguajes.

Ejercitacion desde Geany

r = 10 + 30
print(r)

Hacemos el ejercicio de Laboratorio entre todos.

Estructura de un programa
Programar es como redactar una receta de cocina. Debemos indicarle a la maquina lo que debe hacer. La receta es el programa o aplicación.
Editor de codigo: Es un programa diseñado para permitirnos escribir codigo que crearan nuevos programas. Por ejemplo


Flujo del programa: Recorrido del codigo por el cual las instrucciones se redactan y se interpretan de arriba hacia abajo y de izquierda a derecha. 
Algoritmo: conjunto de operaciones que solucionan un problema determinado. Ej: El procedimiento por el cual se resuelve una ecuación de 2do grado. 


#palabras reservadas
Un bucle while permite repetir la ejecución de un grupo de instrucciones mientras se cumpla una condición (es decir, mientras la condición tenga el valor True). La ejecución de esta estructura de control while es la siguiente: Python evalúa la condición: si el resultado es True se ejecuta el cuerpo del bucle.

#La sentencia condicional if
Se usa para tomar decisiones, este evaluá básicamente una operación lógica, es decir una expresión que de como resultado True o False , y ejecuta la pieza de código siguiente siempre y cuando el resultado sea verdadero.