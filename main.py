# Notebook[{}]
A=10
B=20
C=A+B
print('C: ', C)

def f(x):
    return (x**2)-(2*x)-3
def df(x):
    return (2*x)-2

NoIterMax=100
Tolerancia=0.000001
x0=-0.5
Salir=0
i=0
while (i<=NoIterMax) and (Salir==0):
    print('x0:', x0, 'f(x0)')
    x1=x0-(f(x0)/df(x0))
    if (((x0)==0) or (abs(x1-x0)<=Tolerancia)):
        print("Solución en",i,"Iteraciones")
        print("xsol=",x1)
        Salir=1
    else:
        i=i+1
        x0=x1
    if (i>=NoIterMax):
        print("El método falló")