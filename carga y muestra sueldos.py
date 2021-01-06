m=[]
t=[]
totma=0
tottar=0
for x in range (4):
    v=float(input("ingrese sueldo Turno mañana: "))
    m.append(v)
    totma=totma+m[x]
    
for x in range (4):
    v=float(input("ingrese sueldo Turno tarde: "))
    t.append(v)
    tottar=tottar+t[x]
    
print ("Turno mañana")
for x in range (4):
    print (m[x])
print ("Turno tarde") 
for x in range (4):
    print (t[x])
gral=tottar+totma
print ("gasto general en sueldos: ",gral, "total t mañana: ",totma,"total tarde: ",tottar)
