n=[]
tot=0
for x in range(3):
    v=float(input("ingrese valores: "))
    n.append(v)
    tot=tot+n[x]
print(len(n))
n.sort()
print (n)