import matplotlib.pyplot as plt
import numpy as np

def main():
    # Definimos la función para la cual queremos aproximar la raíz
    def f(x):
        return x**2 - np.cos(x) - 1
    
    # Establecemos el intervalo de la función
    a = 1
    b = 2

    # Establecemos el criterio de parada
    def cifras_significativas(d):
        return (1/2) * (10**-d)

    # Estimamos la cantidad de bisecciones necesarias para aproximarse al resultado con tantas cifras significativas.
    def prediccion_de_bisecciones():
        return np.ceil((np.log(b-a) - np.log(cifras_significativas(4)))/np.log(2))
    
    # Comprobamos el teorema de bolzano en el intervalo
    if f(a) * f(b) < 0:
        print('Para aproximarse a la raiz con una tolerancia de ', cifras_significativas(4), ' se necesitaran ', prediccion_de_bisecciones(), ' bisecciones')
        biseccion = 1
        a_original = a
        b_original = b

        while True:
            # Definimos el punto medio del intervalo y el error.
            m = (a + b) / 2 
            error = (b_original - a_original)/2**biseccion

            # Si la función evaluada en a tiene el mismo signo que la función evaluada en m, entonces cambiamos a por m.        
            if f(a) * f(m) >= 0:
                a = m
            
            # Si la función evaluada en b tiene el mismo signo que la función evaluada en m, entonces cambiamos b por m.
            if f(b) * f(m) >= 0:
                b = m

            # Establecemos el criterio de parada
            if(error < cifras_significativas(4)):
                print("La raiz de la funcion es: ", m)
                break

            biseccion += 1
    else:
        print('El intervalo seleccionado no verifica el teorema de Bolzano')

if __name__ == '__main__':
    main()

