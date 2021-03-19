import matplotlib.pyplot as plt

def Grapher(graphmatrix):
    '''
    Función de graficación genérica, toma una matriz 2xn y
    la grafica utilizando matplot lib.
    Entrada: matriz 2xn que contiene los pares ordenados X,Y
    Salida: gráfico de la relación Y(X)
    '''
    Xplot=graphmatrix[0]
    Yplot=graphmatrix[1]
    plt.plot(Xplot, Yplot)
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Solution')
    plt.show()
    return

def RungeKutta4(x0,y0,function,h,endPoint):
    '''
    Se calcula el y estimado siguiente con espaciado h
    a partir del par ordenado (x0,y0). X y Y son vectores
    de tamaño definido por la distancia y espaciado.
    Entradas:
    x0,y0: condiciones iniciales
    function: función anónima dada por dy/dx
    h: espaciado de la estimación
    endPoint: valor de x a donde se desea estimar
    Salidas:
    [X,Y]: matriz 2xn que incluye los valores de X y Y
    estimados para la solución
    '''
    n=int((endPoint-x0)/h)
    X=[0]*(n+1)
    Y=[0]*(n+1)
    X[0]=x0
    Y[0]=y0
    k=4*[0]
    for i in range(n):
        #Se calculan los valores de k para cada estimación.
        a=X[i]
        b=Y[i]
        k[0]=function(a,b)
        k[1]=function(a+h/2,b+(k[0]*h)/2)
        k[2]=function(a+h/2,b+(k[1]*h)/2)
        k[3]=function(a+h,b+k[2]*h)
        X[i+1]=X[i]+h
        Y[i+1]=b+h*(k[0]+2*k[1]+2*k[2]+k[3])/6
    return [X,Y]

#Los datos utilizados son los indicados en el documento original.
x0=0
y0=101325
L=3000
h=100
df=lambda x,y: (-38.9647*9.8*y*(10**-3))/(8.314462*(293-(x/200)))
[X,Y]=RungeKutta4(x0,y0,df,h,L)
print('resultado:',Y[len(Y)-1])
Grapher([X,Y])
