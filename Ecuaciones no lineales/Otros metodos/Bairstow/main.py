import numpy as np

def main():
    def bairstow(coeficientes, r, s, tolerancia, max_iter):
        n = len(coeficientes) - 1
        iteraciones = 0

        while iteraciones < max_iter:
            # Inicializamos las variables
            b = np.zeros(n + 1)
            c = np.zeros(n + 1)

            # Calculamos los dos primeros valores para b y c
            b[n] = coeficientes[0]
            b[n - 1] = coeficientes[1] + (r) * b[n]
            c[n] = b[n]
            c[n - 1] = b[n - 1] + r * c[n]

            # Calculamos el resto de valores
            for i in range(2, n + 1):
                b[n - i] = coeficientes[i] + (r) * b[n - i + 1] + s * b[n - i + 2]
                c[n - i] = b[n - i] + (r) * c[n - i + 1] + s * c[n - i + 2]

            # Resolvemos las ecuaciones de r y s
            deltaR = ((c[n - 2] * b[n - 5]) - (c[n - 3] * b[n - 4])) / ((c[n - 3]**2) - (c[n - 4] * c[n - 2]))
            deltaS = ((c[n - 4] * b[n - 4]) - (c[n - 3] * b[n - 5])) / ((c[n - 3]**2) - (c[n - 4] * c[n - 2]))
            r = r + deltaR 
            s = s + deltaS

            errorR = np.abs(deltaR / r) * 100
            errorS = np.abs(deltaS / s) * 100

            # Verificamos el criterio de parada
            if errorR < tolerancia and errorS < tolerancia:
                # Calculamos las raíces
                x1 = (r + np.sqrt((r**2) + 4 * s)) / 2
                x2 = (r - np.sqrt((r**2) + 4 * s)) / 2
                return r, s, x1, x2 

            iteraciones += 1

        raise ValueError("El método no converge en el número máximo de iteraciones.")

    # Aplicamos el método de Bairstow a f(x)
    coeficientes = [1, -3.5, 2.75, 2.125, -3.875, 1.25]
    r = -1
    s = -1

    try:
        r, s, x1, x2 = bairstow(coeficientes, r, s, 1, 10)
        print(f"r encontrado: {r}")
        print(f"s encontrado: {s}")
        print(f"Raíces encontradas: x1 = {x1}, x2 = {x2}")
    except ValueError as e:
        print(e)
        
if __name__ == '__main__':
    main()