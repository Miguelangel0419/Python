import itertools
import math

ecuacion = input("ingrese la funcion a resolver: ")
xa = float(input("ingrese la cota inferior: "))
xb = float(input("ingrese la cota superior: "))
tolerancia = float(input("ingrese la tolerancia: "))



def f(X):
    return eval(ecuacion)

    iter = 0
    f_c=999999



    while abs(f_C) >= tolerancia:

        puntoMedio = (xa + xb)/2

        f_a = f(xa)
        f_b = f(xb)
        f_c = f(puntoMedio)


        iter += 1

        print("x_a: ", xa, "x_b: ", xb, "c: ", puntoMedio, "f_c: ", f_c, "Numero de iters: ", iter )

        if( f_a * f_c)<0:
            xb = puntoMedio
        elif ( f_b * f_c)<0:
            xa = puntoMedio
        if abs(f_c)<tolerancia:
            break
        
        
        print ("la raiz buscada es: ", puntoMedio)
        









        
        