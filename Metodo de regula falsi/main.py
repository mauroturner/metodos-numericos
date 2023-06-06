import numpy as np

def main():
    # Definimos la función para la cual queremos aproximar la raíz
    def f(x):
        return x * np.sin(x) - 1
    
    # Establecemos el intervalo de la función
    a = 0
    b = 2

    # Establecemos el criterio de parada
    def cifras_significativas(d):
        return (1/2) * (10**-d)
    
    # Calculamos el punto "c"
    def calcular_c(a, b):
        return (a * f(b) - b * f(a))/(f(b) - f(a))
    
    # Comprobamos el teorema de bolzano en el intervalo
    if f(a) * f(b) < 0:
        c_actual = calcular_c(a, b)
        while True:
            # Si la función evaluada en a tiene el mismo signo que la función evaluada en c, entonces cambiamos a por c.        
            if f(a) * f(c_actual) >= 0:
                a = c_actual
            
            # Si la función evaluada en b tiene el mismo signo que la función evaluada en c, entonces cambiamos b por c.
            if f(b) * f(c_actual) >= 0:
                b = c_actual

            # Definimos el punto "c" nuevo del intervalo, el error y ahora ese c pasará a ser el actual.
            c_nuevo = calcular_c(a, b)
            error = np.abs(c_nuevo - c_actual)/c_nuevo
            c_actual = c_nuevo

            # Establecemos el criterio de parada
            if(error < cifras_significativas(4)):
                print("La raiz de la funcion es: ", c_actual)
                break
    else:
        print('El intervalo seleccionado no verifica el teorema de Bolzano')

if __name__ == '__main__':
    main()