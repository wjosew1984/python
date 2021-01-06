#turno m y t, 4 empleados c/u. Lista sueldo ambos turnos y gasto en sueldo gral.
m=[]
tm=0
for x in range (4):
    v = float(input("Ingrese sueldo: "))
    m.append(v)
    tm = tm+m[x]

t = []
tt=0
for x in range (4):
    v = float(input("ingrese sueldo: "))
    t.append(v)
    tt = tt+t[x]

print("Turno mañana")
for x in range (4):
    print(m[x])
print("turno tarde")
for x in range(4):
    print(t[x])
gral = (tt+tm)
print("Costo total en sueldos: ",gral)