import numpy as np

def main():
    # Definimos la función a integrar
    def f(x):
        return 1 + np.exp(1) ** -x * np.sin(4*x)

    # Definimos los límites de integración
    a = 0
    b = 1

    # Aplicamos la regla 3/8 de Simpson para calcular la integral
    integral = regla_38_Simpson(f, a, b)
    print("Valor aproximado de la integral:", integral)

def regla_38_Simpson(f, a, b):
    h = (b - a) / 3
    c = (2*a + b) / 3
    d = (a + 2*b) / 3
    integral = (3 * h / 8) * (f(a) + 3 * f(c) + 3 * f(d) + f(b))
    return integral

if __name__ == '__main__':
    main()