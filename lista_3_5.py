#4 alumnos, notas de examenes.
#ingresar nombre y nota de alumnos, en dos lsitas paralelas
#crear listado que encuentre los nombres, notas y condicion: MB= nota>=8, B= entre 4 y 7, INS=<4
#imprimir cuantos MB


alumnos=[]
t=0
notas=[]
n=0
MB=("muy bien")
B=("bien")
INS=("desaprobado")
curso=[[alumnos],
       [notas]
       ]

for x in range(4):
    v=str(input("Ingrese Nombre de alumno: "))
    alumnos.append(v)

for x in range(4):
    v=float(input("Ingrese nota de exámen: "))
    notas.append(v)
    n=n+notas[x]

for x in range(4):
    if notas[x]>=8:
        print(alumnos[x],notas[x],MB)
    else:
        if notas[x]>=4 and notas[x]<=7:
            notas[x]=B
        else:
            notas[x] = INS