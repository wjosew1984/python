Proyecto Integrador de clase 4
Solucion
import os
 
alumnos = {}
aux = 0
 
while(True):
    print("\nIngrese el nro de la operacion que desea ejecutar: ")
    print("1- Ver la lista de alumnos.")
    print("2- Añadir un alumno a la lista.")
    print("3- Ver la cantidad de cursos de un alumno.")
    print("4- Salir.")
 
    valor = int(input(""))
    os.system("cls")
    
    if(valor==1):
        if(aux==1):
            print("Lista de Alumnos: ")
            for alumno in alumnos:
                nomb = alumno
                cur = alumnos[alumno]
                print(nomb + " - ", str(cur)+" cursos")
        else:
            print("No hay alumnos en la lista.")
    elif(valor ==2):
        
        nombre = input("Ingrese el nombre de un alumno: ")
        cant_cursos = int(input("Cantidad de cursos inscriptos: "))
        
        alumnos[nombre]=cant_cursos
 
 
        aux=1
        print("¡El alumno fue añadido a la lista!")
    
    elif(valor == 3):
        os.system("cls")
        aux1=True
        while(aux1==True):
            nombre = input("Ingrese el nombre del alumno: ")
            if(nombre==""):
                print("No ingreso dato alguno, vuelva a intentar")
            else:
                print("El alumno "+ nombre + " tiene ", alumnos[nombre], "cursos asignados")
                aux1=False
        
    elif(valor == 4):
        os.system("cls")
        print("¡Gracias por utilizar el programa!")
        break    
    
    else:
        os.system("cls")
        print("La opcion ingresada no es correcta, vuelva a intentarlo")
                                               
                                             CLASE 5 – Aplicaciónes de Escritorio

Conceptos básicos de aplicación de escritorio

Se trata de un programa que establece una interacción con el usuario a través de una interfaz gráfica. Las aplicaciones web también cumplen con este requisito pero se corren a través del navegador sin utilizar los recursos nativos de nuestra computadora.
Ej de aplicaciones de escritorio: Geany, Firefox, Chrome, Word, Excel, Explorador de Windows (aplicaciones de escritorio). Nos focalizaremos en este tipo de aplicaciones.


Ventana (Ej de aplicación de escritorio)



Vemos botones, etiquetas, grilla, lista desplegable, textarea, labels.


Controles

Son los componentes de una interfaz grafica (Widgets). Ej botones, cajas de texto, menues, tabla o grilla, lista desplegable, etiquetas y las ventanas. 
Un control o widget entonces es cualquier componente grafico por el cual puedo interactuar con una aplicación de escritorio.


Tcl/Tk (Modulo Tkinter)

Es la Biblioteca que nos brindara las herramientas para elaborar aplicaciones de escritorio. La importamos:

import tkinter as tk
Tk es la de menor complejidad orientada a aplicaciones pequeñas y medianas.
Tk es la biblioteca que es utilizada también por otros lenguajes de programación. En Python la herramienta que utilizamos para aplicar esta biblioteca es tkinter.


Creamos nuestra primer ventana

#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tkinter as tk                          #la renombramos utilizando un alias como tk
 
                                              #Creamos el control principal (que es la ventana)
 
ventana = tk.Tk()                             #se crea la ventana y se guarda en una variable.
                                              #Tk() es una funcion que se encuentra dentro de
                                              #la biblioteca tk y me permite crear la ventana.
                                              #El resultado de la funcion Tk() es una referencia
                                              #a la ventana. Y guardo esa referencia en la variable
                                                                                            
                                              #todos los controles van entre esta instruccion y mainloop
 
ventana.config(width=600, height=400)
 
ventana.title("Hola a Todos")                 # le da un nuevo titulo a la ventana
 
ventana.mainloop()                             #hace visible la ventana. La funcion mainloop() bloquea
                                               #la ejecucion del codigo hasta que ocurra un evento determinado.
                                               #Al igual que input() cuyo evento era el enter. Para mainloop()  
                                               #se bloquea el codigo hasta que el usuario cierra la ventana.
                                               #Ver print() siguiente
                                                 
print("Esto aparecera despues de cerrar la ventana")                                              
                                               #despues de la funcion mainloop() el |codigo que podria existir
                                               #es el cierre de un archivo o conexion de la base de datos.


Agregamos los diferentes controles


Crear un control=>1. Crear una variable. 2. Escoger el tipo de control. 3. Darle un tamaño. 4. Ubicarlo en la Interfaz (Posicion en pixeles).

Resumidamente para crear controles, primero creamos la variable y segundo asignamos la posición y tamaño con place()

botón (tk.Button), caja de texto (tk.Entry) y etiqueta (tk.Label) 
Cabe mencionar que las funciones que crean los controles en tk, siguen la convencion de la primera letra en mayuscula. A diferencia de las funciones de consola.
#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tkinter as tk                
ventana = tk.Tk()   
                          
ventana.title("Controles")
ventana.config(width=400, height=400)         #configuramos el tamaño de la ventana, px
 
#Boton
boton = tk.Button(text="Boton")                
boton.place(x=50, y=30, width=100, height=40)  #coordenadas de posicion del boton en la ventana=> x=50 y=50 
                                               #tamaño del boton => width y height
 
#Caja de texto(Entry) => 
#analogo al input() de consola => TextBox
caja = tk.Entry()                              #Entry() en este caso no requiere argumento
caja.place(x=20, y=120, width=150, height=25)
 
 
#Etiqueta (Muestran texto como la barra de estado de Geany. Y mensajes en tiempo de ejecucion)
 
etiqueta = tk.Label(text="Nombre", bg="#8B6914") #La etiqueta no le colocamos un Width o Height para que se
                                                #adecue al tamaño del texto. tk lo calcula automaticamente
etiqueta.place(x=20, y=98)                      #Por defecto el fondo de la ventana y de las etiquetas es el mismo
                                                #Con el argumento "bg" puedo establecer otro color de fondo.
                                                #En geany tenemos el boton Selector de Color para generar el mismo.
 
ventana.mainloop()


A continuacion vemos la imagen de posición (x, y) y tamaño (width, height):
    


Interaccion con la Interfaz Grafica (Funcionalidad a los controles)
Boton: Realiza una determinada acción cuando el usuario lo presiona.

Ejercicio para hacer entre todos - a
Por ejemplo didácticamente podemos definir una función que se llame botón_presionado() a partir de la cual me permita imprimir (“Hola Mundo”) por consola cuando el usuario presione el boton. 
Agregar el argumento command el cual llamara a la función.

Caja de Texto: Recibe información que el programa usara de una u otra forma.
Ejercicio para hacer entre todos - b
Hacer que el texto que se ingrese en la caja de texto, cuando se oprima el botón, aparezca en la consola. 
Entonces dentro de la def de la función botón_presionado utilizar la función get() para tal efecto.

Este paradigma de programación es Programacion Orientada a Eventos.

Instrucción delete

delete(index1, index2=None)

Ej: tenemos el siguiente código con un textbox, un botón y un label. La idea es que el usuario ingrese un valor y dicho valor aparezca en un label. Una vez que apareció el texto que el usuario había ingresado se borre.

import tkinter as tk
 
def borrar():
  
    aux = caj.get("0.0", "end")
    lbl1.config(text=aux)
    caj.delete("0.0", "end")
 
ventana = tk.Tk()
 
ventana.title("Bienvenido a nuestra aplicacion")
ventana.config(width=400, height=400)
lbl = tk.Label(text="Dia actual")
lbl.place(x=20, y=40)
 
caj = tk.Text()
caj.place(x=100, y=40, width=100, height=20)
 
btn = tk.Button(text="Aceptar", bg="orange", fg="red", command=borrar)
btn.place(x=70, y=100)
 
lbl1 = tk.Label()
lbl1.place(x=70, y= 140)
 
ventana.mainloop()




Ejercicio de Laboratorio – Calculadora - c





Proyecto Integrador







Variables y Ambitos (scope)

Por ámbito entendemos el lugar o espacio en el que una variable es reconocida como tal, o el lugar en donde una variable es visible para otras porciones de código.

Variables locales: Son aquellas que se crean dentro de las funciones y no podrán ser llamadas por afuera. 

Ej: 
def boton_presionado():
    var = 12
    return var
    
print(boton_presionado())
print(var)
Variables Globales: Son las que no están definidas dentro de la función y podrán ser accedidas desde cualquier lugar del código.

def f(): 
    a = 1 
    print(a) 
    print(b) 
 
b = 2 
f()

Es una buena práctica de la programación crear variables únicamente en el ámbito en el que son requeridas.

Dos variables con el mismo nombre pueden coexistir si pertenecen a ámbitos distintos:

def f():
    b= 7
    print(a + b)
 
a = 5
print(a)
b=10
f()
 
print(b)
