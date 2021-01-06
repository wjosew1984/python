
lista=[10,5,8,20,30]
k=lista[0]
for x in range (1,len(lista)):
    if lista[x]>k:
        k=lista[x]
print (k)
"""
lista=[10,5,8,20,30]
lista.append(12)
print(lista)
"""
lista=[10,5,8,20,30,12]
lista.pop(0)
print(lista)

lista=[10,5,8,20,30,12]
lista.pop(-1)
print(lista)