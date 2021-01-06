#numero1 = int(input("ingrese un numero:"))
#numero2 = int(input("ingrese un numero:"))
#print(numero1+numero2)

#n1 = int(input("Ingrese un numero por favor"))
#n2 = int(input("Ingrese un numero por favor"))
#print(" El resultado es" , n1 + n2)

#alum1_nomb = input("Ingrese su nombre completo ")
#alum1_edad = input("Ingrese su edad ")
#print(alum1_nomb , alum1_edad , " años ha sido ingresado correctamente")

"""
n1 = 4
n2 = 10
promedio = ((n1 + n2) / 2) 
print(promedio)
"""
"""
suma = 0
for i in range(0,5):
    suma = int(input("Ingrese un numero" , + suma))
    print(suma)
"""
"""name = "Jose Luis"
#apellido = "Medina"
edad = "36"
"""
"""print("Estudiante " + name , apellido , "de" , edad , "años")"""
#mensaje_final = "Se inscribio correctamente al estudiante"
#print(mensaje_final, name , apellido , "de" , edad , "años")

#my_string = "Curso de Codigo Python por Jose Luis" 

"""print(my_string)
print(my_string[9])
print(my_string[0], my_string[-1]) #muestra la primera posicion y la ultima del string
print(my_string[0:10]) #donde empieza y termina
print(my_string[5:12]) #donde empieza y termina
print(my_string[-2:-1])
print(my_string[0:10:2]) #donde empieza, donde termina y muestra de 2 en 2
print(my_string[::-1]) #se lee el string de derecha a izquierda
print(my_string[::1]) #se lee el string de derecha a izquierda
"""
course = "Curso"
my_string = "Codigo de Python por Jose"

"""result = "{} de {}".format(course, my_string)
print(result)
"""
result = "{a} de {b}".format(b = course, a = my_string)
print(result)

#result = result.lower () #Codigo de Jose minuscula 
#result = result.upper () #Codigo de Jose mayuscula
#result = result.title () #Codigo de Jose titulo
#print(result)

#pos = result.find("codigo")
#print(pos)
#print(result[9])

course = "Curso"
my_string = "Codigo de Python por Jose"

#"""pos = result.find("Codigo")
#count = result.count("C")

#print(count)
#"""
"""
new_string = "Curso Codigo de Python por Jose"
new_string = result.replace("C", "x") # reemplaza por la segunda opcion
new_string = result.split(" ") # seccionado en partes
print(new_string) 
"""
"""
#- listas
my_list = ["strings", 15, 15.6, True]
my_list.append(6) #agrega un dato (number al final)
my_list.insert(1, "insert") #agrega primero un numero entero 
my_list.remove(15) #remueve un dato 
my_list.pop() #remueve ultimo dato 
my_list = [1,9,22,6,8,65,14,99] #lista desordenada
print(my_list)
my_list.sort() #ordena la lista en forma ascendente
print(my_list)
my_list.sort(reverse=True) #ordena la lista en forma descendente
print(my_list)

my_list = [1,9,22,6,8,65,14,99]
my_list_two = [22, 23]

my_list.extend(my_list_two) #une dos listas en una

print(my_list) #cuando vuelvo a imprimir deberia mostrar las dos listas en una

my_list.extend(my_list_two) #une dos listas en una
my_list.append(my_list_two) #une dos listas en una pero con llaves (como lista)

#- tuplas () permiten almacenar datos, objetos, diferencia es que son inmutable, no pueden modificar (password, permisos de acceso,ruta especifica, cosas que no van a ser modificadas en el transcurso del proyecto)
# - listas []
my_tuple = (1,"string", True)
print(my_tuple)
print(my_tuple[0:3])
print(my_tuple[0:2])
"""
"""
#diccionarios estructura de datos podemos almacenar string, numbers, tuplas, listas (datos inmutables, se pueden modificar y se va a ver solo el ultimo)
diccionario = { "a" : True, 5: "esto es un string", "a":100, "a": False}

diccionario ["c"] = "nuevo string" #crea clave/ valor
diccionario ["a"] = False #Si la llave/clave se encuentra, actualiza sino crea
#valor = diccionario["z"] #Obtenemos los valores
valor = diccionario.get("a",(12,2)) #get

del diccionario[5] # del se usa para eliminar

print(diccionario)
print(valor)

llaves = list( diccionario.keys()) #objeto iterable
valores = list( diccionario.values())
#llaves = tuple( diccionario.keys()) #objeto iterable
#valores = tuple( diccionario.values())

diccionario_dos = {"z":23, "w":88}
diccionario["z"] = diccionario_dos["z"]
diccionario["w"] = diccionario_dos["w"]

#print(llaves)
#print(valores)
print(diccionario)
"""
#condicionales # ,> < >= <= != ==

"""
fruta = "kiwi"
if (condicion):
tab (identamos+codigo)

fruta = "kiwi"
if fruta =="kiwis": #Si solo si
  print ("El valor es kiwi")
else:
  print ("No son iguales")

mensaje = "El valor es kiwi" if fruta == "kiwi" else "No son iguales"
print(mensaje)


fruta = "manzana"

if fruta =="kiwis": #Si solo si
  print ("El valir es kiwi")

elif fruta == "manzana": #no olvidarse los :
  print("Es una manzana")

else:
  print ("No son iguales")

mensaje = "El valor es kiwi" if fruta == "kiwi" else "No son iguales"
print(mensaje)

#True=1
#False=0

if 0:
  print("Es verdad")
else:
  print("No es verdad")
print(0)

if []: #vacio es falso
      print("Es verdad")
else:
  print("No es verdad")
print(0)

#True=1
#False=0

valor = None #toma valor de cero y es falso
valor_dos = 21

if valor and valor_dos > 20:  #and deben cumplirse las dos condicionales
  print("Es verdad")
else:
  print("No es verdad")

#True=1
#False=0

valor = None #toma valor de cero y es falso
valor_dos = 21

if valor or  valor_dos > 20:  #si una condicionales es verdadera, se vuelve verdadera toda la condicion 
  print("Es verdad")
else:
  print("No es verdad")
"""
"""
# ciclos while
contador = 0

#while (contador)  <10: # > => < <= == != ciclo infinito porque cero es siempre menor que 10
#   print(contador)
#else: 
#   print("El while a terminado")
"""
"""
while (contador)  <10: # > => < <= == !=
   print(contador)
   contador +=1 #Aumenta en 1 el contador #contador = contador + 1
else: 
   print("El while a terminado")
"""
"""
#listas
lista = (1,2,3,4,5,6,7,8,9,10)
"""
"""
for i in lista:
  pass
new_range = range(0,20,2)#(0,20,3)(0,20,4)
for i in new_range:
  print(new_range)
"""
"""
indice = 0
for valor in lista:
  print(valor, "tiene el indice", indice)
  indice +=1

for valor in range(0, len(lista)):
       pass#print(valor, "tiene el indice", indice)

for valor in "Curso de Codigo Facilito": #los strings son iterables
   print(valor)

#diccionario
diccionario = {"a":10, "b":20, "c":500}
for llave, valor in diccionario.items():
   print("la llave", llave, "tiene el valor de", valor)

#lista con 100 valores List Comprehension

Lista = [valor for valor in range (0,101)]
print(Lista)

#lista con 100 valores solo los pares

Lista = [valor for valor in range (0,101) if valor % 2 == 0]
print(Lista)

tupla =  tuple( (valor for valor in range (0,101) if valor % 2 != 0) )
print(tupla)

diccionario = {indice:valor for indice, valor in enumerate(lista) if indice < 10}
diccionario = {indice:valor for indice, valor in enumerate(lista)}
print(diccionario)
"""
n1 = int(input("Ingrese año actual, "))
n2 = int(input("Ingrese año_nacimiento, "))
edadactual = (n1-n2)
print("Su edad es " , edadactual, "años")
"""
numero = 5
alumno = "El mejor alumno\n de este año es: "
#alumno = "El mejor alumno\n\t de este año es: "
print(type(numero))
factorial = 1 
while numero > 0:
   factorial = factorial * numero
   numero -=1
print(factorial)
print(alumno)


numero = 5 
alumno = "El mejor alumno\t de este año es: "
ofertas = True
print(type(numero))
print(type(alumno))
print(type(ofertas))
"""