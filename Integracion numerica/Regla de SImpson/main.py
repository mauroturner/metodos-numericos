import numpy as np

def main():
    # Definimos la función a integrar
    def f(x):
        return 1 + np.exp(1) ** -x * np.sin(4*x)

    # Definimos los límites de integración
    a = 0
    b = 1

    # Aplicamos la regla de Simpson para calcular la integral
    integral = regla_de_Simpson(f, a, b)
    print("Valor aproximado de la integral utilizando la regla de Simpson:", integral)

def regla_de_Simpson(f, a, b):
    h = (b - a) / 2
    c = (a + b) / 2
    integral = (h / 3) * (f(a) + 4 * f(c) + f(b))
    return integral

if __name__ == '__main__':
    main()
