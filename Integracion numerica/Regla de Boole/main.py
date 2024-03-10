import numpy as np

def main():
    # Definimos la función a integrar
    def f(x):
        return 1 + np.exp(1) ** -x * np.sin(4*x)

    # Definimos los límites de integración
    a = 0
    b = 1

    # Aplicamos la regla de Boole para calcular la integral
    integral = regla_de_Boole(f, a, b)
    print("Valor aproximado de la integral:", integral)

def regla_de_Boole(f, a, b):
    h = (b - a) / 4
    c = a + h
    d = a + 2 * h
    e = a + 3 * h
    integral = (2 * h / 45) * (7 * f(a) + 32 * f(c) + 12 * f(d) + 32 * f(e) + 7 * f(b))
    return integral

if __name__ == '__main__':
    main()
