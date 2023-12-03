import numpy as np

def main():
    # Definimos el sistema de ecuaciones
    A = np.array([
        [3, -1, -1],
        [-1, 3, 1],
        [2, 1, 4]
    ])

    b = np.array([1, 3, 7])

    # Establecemos el criterio de parada
    def cifras_significativas(d):
        return (1/2) * (10**-d)

    def metodo_jacobi(A, b, x0, tolerancia, max_iter):
        n = len(b)
        x = x0.copy()
        x_prev = x0.copy()
        iteraciones = 0

        while iteraciones < max_iter:
            for i in range(n):
                sigma = np.dot(A[i, :n], x_prev[:n]) + np.dot(A[i, n:], x_prev[n:])
                x[i] = (b[i] - sigma + A[i, i] * x_prev[i]) / A[i, i]

            # Verificamos el criterio de parada (Norma infinito vs. cantidad de cifras significativas requeridas)
            if np.linalg.norm(x - x_prev, np.inf) < tolerancia:
                return x, iteraciones

            x_prev = x.copy()
            iteraciones += 1

        raise ValueError("El método no converge en el número máximo de iteraciones.")

    # Aplicamos el método de Jacobi al sistema de ecuaciones
    x0 = np.zeros_like(b, dtype=float)
    try:
        solucion, iteraciones = metodo_jacobi(A, b, x0, cifras_significativas(8), 100)
        print("Solución encontrada:")
        print(solucion)
        print(f"Iteraciones: {iteraciones}")
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()
