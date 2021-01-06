e=0
a=1
cant=int(input("ingrese la cantidad de alumnos: "))
while cant>=a:
    edad=int(input("ingrese la edad del alumno: "))
    print(a)
    a=a+1
    e=edad+e
    promedio=e/cant
print("la edad promedio es de: ",promedio)
