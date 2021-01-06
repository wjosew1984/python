n=[]
tot=0
for x in range (5):
    v=float(input("ingrese estatura"))
    n.append(v)
    tot=tot+n[x]
    promedio=tot/5
print ("el promedio es: ",promedio)
for x in range (5):
    if n[x]>promedio:
        print(n[x],"es mas alto que el promedio")
    else:
        print(n[x],"es mas bajo")
