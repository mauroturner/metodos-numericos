import numpy as np

def main():
    # Definimos la función para la cual queremos aproximar la raíz
    def f(x):
        return (x**2) - np.cos(x) - 1
    
    # Establecemos el intervalo de la función
    x0 = -1
    x1 = -2

    # Establecemos el criterio de parada
    def cifras_significativas(d):
        return (1/2) * (10**-d)
    
    def secante(funcion, x0, x1, tolerancia, max_iter):
        iteraciones = 0
        
        while iteraciones < max_iter:
            f_x0 = funcion(x0)
            f_x1 = funcion(x1)
            
            # El denominador no puede ser 0
            if f_x1 - f_x0 == 0:
                raise ValueError("La secante resulta en un denominador cero.")
            
            x_nueva = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
            
            # Verificamos el criterio de parada
            if np.abs(x_nueva - x1) < tolerancia:
                return x_nueva, iteraciones
            
            x0 = x1
            x1 = x_nueva
            iteraciones += 1
        
        raise ValueError("El método no converge en el número máximo de iteraciones.")
    
    try:
        raiz, iteraciones = secante(f, x0, x1, cifras_significativas(5), 10)
        print(f"Raíz encontrada: {raiz}")
        print(f"Iteraciones: {iteraciones}")
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()