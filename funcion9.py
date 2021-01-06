def entradas():
    nom=[]
    ed=[]
    for x in range(5):
        f=str(input("ingrese su nombre: "))
        nom.append(f)
        v=int(input("ingrese su edad: "))
        ed.append(v)
    return nom,ed

def prom(ed):
    for x in range(len(ed)):
        tot=0
        tot=tot+ed[x]
        prom=tot/5
    return prom


def salidas(nom,ed):
    for x in range(len(ed)):
        if ed[x]>18:
            print(nom[x],ed[x])

nombres,edades=entradas()
promedio=prom(edades)
salidas(nombres,edades)
print(promedio)   
