def carga():
    sueldo=[]
    for x in range(3):
        f=int(input("Ingrese valor: "))
        sueldo.append(f)
    return sueldo

def impsueldo(sueldo):
    print("lista de sueldos: ")
    for x in range(len(sueldo)):
          print(sueldo[x])

def mayor40k(sueldo):
          tot=0
          for x in range(len(sueldos)):
              if sueldo[x]>40000:
                  tot=tot+1
          print(tot)
         
          
def prom(sueldo):
    tot=0
    for x in range(len(sueldo)):
        tot=tot+sueldo[x]
        prom=tot/len(sueldo)
    return prom

def inferprom(sueldo):
    p=prom(sueldo)     
    print("inferior a 40000: ")
    for x in range(len(sueldo)):
        if sueldo[x]<p:
          print (sueldo[x]) 
        
sueldos=carga()
impsueldo(sueldos)
mayor40k(sueldos)
inferprom(sueldos)
