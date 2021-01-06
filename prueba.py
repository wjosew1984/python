def cargar_empleados():
    empleados = []
    for x in range(1):
        nom = input("Ingrese el nombre del empleado:")
        su1 = int(input("Primer sueldo:"))
        su2 = int(input("Segundo sueldo:"))
        su3 = int(input("Tercer sueldo:"))
        empleados.append([nom, (su1, su2, su3)])
    print (empleados)

cargar_empleados()