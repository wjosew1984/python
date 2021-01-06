"""a=2
b=3
c=a+b
print("El resultado es", c)


nombre="Adrian"
apellido="Jusid"

print(nombre+" "+apellido)

print(nombre, apellido)
edad=36
print("soy" , nombre , apellido , "y tengo ", edad , "años")


a=100
b=1000
c=10000

print(a>b)

print(True and True) 
print(True and False) 
print(False and True) 
print(False and False) 

num=int(input("Ingrese un numero por favor:"))
if num==100:
    print("numero igual a cien")
else:
    if num > 100:
        print("numero mayor a cien")
    else:
        print("numero menor a cien")
#print("Se ejecuta siempre, fuera del bloque")
tuplas ordenadas y no se pueden modificar
tupla=(10,20,30,40,50,60)
print(tupla[3])
t1=(5,6)
t2=(7,8)
t3=t1+t2
print(t3)

#listas no son ordenadas y se pueden modificar

lista=[10,20,30,40,50]
print(lista[2])
lista[2]=35
print(lista)


lista=[10,20,30,40,50]
lista.append(60)
print(lista)
lista.insert(2,25)
print(lista)
lista.remove(60)
print(lista)
quitado=lista.pop(4)
print(quitado)
print(lista)
lista.pop(4)
print(lista)

print(len(lista))

lista=[10,20,30,40,50]
for elemento in lista:
    print(elemento)

#range(desde, hasta, incremento)
i=3
for i in range(0,5,1)
range(0,5,1) -> [0,1,2,3,4,] range(0,5)
range(0,5,2) -> [0,2,4,] 
range(1,10,1) -> [1,2,3,4,5,6,7,8,9] 
range(5,-1,-1) -> [5,4,3,2,1,0] 

lista=[]
valor=0
for i in range(0,4,1):
    valor=valor+10
    lista.append(valor)
print(lista)

for valor in range(0,4,1):
    valor=valor+10
    lista.append(valor)
print(lista)


matriz=[["a","b","c"], ["d","e","f"]]
for lista in matriz:
    for elemento in lista:
        print(elemento)
"""
num=1
while num<10:
    print(num)
    num+=1
    if num==5:
        break
