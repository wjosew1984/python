def suma():
    n1=int(input("Ingrese un numero: "))
    n2=int(input("ingrese un numero: "))
    s=n1+n2
    print(s)
def resta():
    n1=int(input("Ingrese un numero: "))
    n2=int(input("ingrese un numero: "))
    s=n1-n2
    print(s)
def multi():
    n1=int(input("Ingrese un numero: "))
    n2=int(input("ingrese un numero: "))
    s=n1*n2
    print(s)
def div():
    n1=int(input("Ingrese un numero: "))
    n2=int(input("ingrese un numero: "))
    s=n1/n2
    print(s)

x=input("¿qué operación desea realizar?: (+,-,*;/)")
if x == "+":
    suma()
else:
    if x=="-":
        resta()
    else:
        if x=="*":
            multi()
        else:
            if x=="/":
                div()
            else:
                print("error")
