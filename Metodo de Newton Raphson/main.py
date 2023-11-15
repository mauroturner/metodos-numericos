import numpy as np

def main():
    # Definimos la función para la cual queremos aproximar la raíz
    def f(x):
        return (x**2) - np.cos(x) - 1
    
    def derivada_f(x):
        return 2*x + np.sin(x)
    
    # Establecemos el intervalo de la función
    a = 1
    b = 2

    # Establecemos el criterio de parada
    def cifras_significativas(d):
        return (1/2) * (10**-d)
    
    def newton_raphson(funcion, derivada, x0, tolerancia, max_iter):
        x = x0
        iteraciones = 0
        
        while iteraciones < max_iter:
            x_nueva = x - funcion(x) / derivada(x)
            
            # Verificamos el criterio de parada
            if np.abs(x_nueva - x) < tolerancia:
                return x_nueva, iteraciones
            
            x = x_nueva
            iteraciones += 1
        
        raise ValueError("El método no converge en el número máximo de iteraciones.")
    
    # Aplicamos el método de Newton Raphson a f(x)
    x0 = 1.5
    try:
        raiz, iteraciones = newton_raphson(f, derivada_f, x0, cifras_significativas(5), 10)
        print(f"Raíz encontrada: {raiz}")
        print(f"Iteraciones: {iteraciones}")
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()