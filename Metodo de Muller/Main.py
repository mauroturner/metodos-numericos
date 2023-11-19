import numpy as np

def main():
    # Definimos la función para la cual queremos aproximar la raíz
    def f(x):
        return (x**3) - (13*x) - 12

    # Establecemos el criterio de parada
    def cifras_significativas(d):
        return (1/2) * (10**-d)
    
    def muller(funcion, x0, x1, x2, tolerancia, max_iter):
        h0 = x1 - x0
        h1 = x2 - x1
        d0 = (funcion(x1) - funcion(x0)) / h0
        d1 = (funcion(x2) - funcion(x1)) / h1
        d = (d1 - d0) / (h0 + h1)
        
        iteraciones = 0
        while iteraciones < max_iter:
            b = (h1 * d) + d1
            D = np.sqrt(b**2 - 4*funcion(x2)*d)
            
            if np.abs(b - D) < np.abs(b + D):
                E = b + D
            else:
                E = b - D
            
            h = (-2 * funcion(x2)) / E
            x3 = x2 + h
            
            if np.abs(h) < tolerancia:
                return x3, iteraciones
            
            x0 = x1
            x1 = x2
            x2 = x3
            
            h0 = x1 - x0
            h1 = x2 - x1
            d0 = (funcion(x1) - funcion(x0)) / h0
            d1 = (funcion(x2) - funcion(x1)) / h1
            d = (d1 - d0) / (h0 + h1)
            
            iteraciones += 1
        
        raise ValueError("El método no converge en el número máximo de iteraciones.")

    # Aplicamos el método de Muller a f(x)
    x0 = 4.5
    x1 = 5.5
    x2 = 5

    try:
        raiz, iteraciones = muller(f, x0, x1, x2, cifras_significativas(5), 10)
        print(f"Raíz encontrada: {raiz}")
        print(f"Iteraciones: {iteraciones}")
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()