#Carga de 2 listas numericas enteras de 4 elementos cada una. generar una lista que surja de la suma de los elementos de la misma posicion de c/lista. mostrar la 3er lista
notas=[]
n=0
MB=("muy bien")
B=("bien")
INS=("desaprobado")
for x in range(4):
    v=float(input("Ingrese nota de exámen: "))
    notas.append(v)
    n=n+notas[x]

for x in range(4):
    if notas[x]>=8:
        notas[x]=MB
        print(MB,)
    else:
        if notas[x]>=4 and notas[x]<=7:
            notas[x]=B
        else:
            notas[x] = INS
