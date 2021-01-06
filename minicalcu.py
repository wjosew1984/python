def suma():
    n1=int(input("ingrese primer numero :"))
    n2=int(input("ingrese segundo numero :"))
    s=n1+n2
    print(s)
def resta(n1,n2):
    s=n1-n2
    print(s)
def multip(n1,n2):
    s=n1*n2
    return s
def divi (n1,n2):
    s=n1/n2
    return s

x=input("que operacion desea hacer(+,-,*,/)?")
if x=="+":
    suma()
else:
    if x=="-":
        q=int(input("ingrese primer numero :"))
        w=int(input("ingrese segundo numero :"))
        resta(q,w)
    else:
        if x=="*":
            q=int(input("ingrese primer numero :"))
            w=int(input("ingrese segundo numero :"))
            s=multip(q,w)
            print(s)
        else:
            if x=="/":
                q=int(input("ingrese primer numero :"))
                w=int(input("ingrese segundo numero :"))
                s=divi(q,w)
                print(s)
            else:
                print("error")
            
