import numpy as np

def main():
    # Definimos la función para la cual queremos aproximar la raíz
    def f(x):
        return (np.exp(1) ** x) - 4 + x
    
    # Convertimos f(x) a x = g(x)
    # Opción 1
    def g(x):
        return 4 - (np.exp(1) ** x)
    
    # Opción 2
    def h(x):
        return (np.exp(1) ** x) - 4 + 2 * x
    
    # Opción 3
    def j(x):
        return np.log(4 - x)
    
    # Establecemos el intervalo de la función
    a = 1
    b = 2

    # Establecemos el criterio de parada
    def cifras_significativas(d):
        return (1/2) * (10**-d)
    
    def punto_fijo(funcion, x0, tolerancia, max_iter):
        x = x0
        iteraciones = 0
        
        while iteraciones < max_iter:
            x_nueva = funcion(x)
            
            # Verificamos el criterio de parada
            if np.abs(x_nueva - x) < tolerancia:
                return x_nueva, iteraciones
            
            x = x_nueva
            iteraciones += 1
        
        raise ValueError('El método no converge en el número máximo de iteraciones.')
    
    # Aplicamos el método del punto fijo a la función j(x)
    x0 = 1
    tolerancia = cifras_significativas(2)
    max_iter = 10
    
    try:
        raiz, iteraciones = punto_fijo(j, x0, tolerancia, max_iter)
        print(f"Raíz: {raiz}")
        print(f"Número de iteraciones: {iteraciones}")
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()