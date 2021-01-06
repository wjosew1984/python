m=int(input("ingrese cantidad de comensales: "))
if m>200:
    if m>=300:
        p=m*70
    else:
        p=m*80
else:
    p=m*95
print("el costo por la cantidad de platos es: $",p)
