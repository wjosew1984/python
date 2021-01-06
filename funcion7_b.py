#se puede hacer con un "if" para no hacer dos "for"

def maymen(lis):
    ma=lis[0]
    me=lis[0]
    for x in range(1,len(lis)):
        if lis[x]>ma:
            ma=lis[x]
        else:
            if lis[x]<me:
                me=lis[x]
    print (ma, " es el mayor", me," es el menor")


lis = []
for x in range(5):
    v = int(input("Ingrese 5 enteros: "))
    lis.append(v)

maymen(lis)