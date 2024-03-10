import numpy as np

def main():
    # Definimos la función a integrar
    def f(x):
        return 1 + np.exp(1) ** -x * np.sin(4*x)

    # Definimos los límites de integración
    a = 0
    b = 1

    # Aplicamos la regla del trapecio para calcular la integral
    integral = regla_del_trapecio(f, a, b)
    print("Valor aproximado de la integral: ", integral)

def regla_del_trapecio(f, a, b):
    h = (b - a) / 2
    integral = h * (f(a) + f(b)) 
    return integral

if __name__ == '__main__':
    main()