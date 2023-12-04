import numpy as np

def main():
    # Definimos el sistema de ecuaciones
    A = np.array([
        [9, 2, -1],
        [7, 8, 5],
        [3, 4, -10]
    ])

    b = np.array([-2, 3, 6])

    # Establecemos el criterio de parada
    def cifras_significativas(d):
        return (1/2) * (10**-d)

    def gauss_seidel(A, b, x0, tolerancia, max_iter):
        n = len(b)
        x = x0.copy()
        iteraciones = 0

        while iteraciones < max_iter:
            x_prev = x.copy()

            for i in range(n):
                suma1 = np.dot(A[i, :i], x[:i])
                suma2 = np.dot(A[i, i + 1:], x_prev[i + 1:])
                x[i] = (b[i] - suma1 - suma2) / A[i, i]

            # Verificamos el criterio de parada (Norma infinito vs. cantidad de cifras significativas requeridas)
            if np.linalg.norm(x - x_prev, np.inf) < tolerancia:
                return x, iteraciones

            iteraciones += 1

        raise ValueError("El método no converge en el número máximo de iteraciones.")

    # Aplicamos el método de Gauss-Seidel al sistema de ecuaciones
    x0 = np.zeros_like(b, dtype=float)
    try:
        solucion, iteraciones = gauss_seidel(A, b, x0, cifras_significativas(5), 100)
        print("Solución encontrada:")
        print(solucion)
        print(f"Iteraciones: {iteraciones}")
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()