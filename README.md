# Métodos numéricos
Los métodos numéricos son aquellas técnicas y algoritmos para resolver problemas matemáticos de manera aproximada utilizando cálculos numéricos y computacionales. Estos métodos son especialmente útiles cuando no es posible obtener una solución exacta o analítica utilizando métodos algebraicos o cuando los cálculos analíticos son demasiado complejos o costosos computacionalmente.

## Cifras significativas

### ¿Qué es?
Las cifras significativas son dígitos de un número que consideramos no nulos. **(No es lo mismo que cantidad de decimales)**.

### Objetivo
Cuando se emplea un número para realizar un cálculo, debe haber seguridad de que pueda usarse con confianza. Las cifras significativas de un número son aquellas que pueden utilizarse en forma confiable. Se trata del número de dígitos que se ofrecen con certeza, más uno estimado.

A la omisión del resto de cifras significativas se le conoce como **error de redondeo**.

### Reglas prácticas
- Los 0 a la derecha no definen una cantidad de C.S.
- Cualquier dígito distinto de 0 es significativo
- Los 0 a la izquierda de la primera C.S no es significativo
- Los 0 entre dígitos son significativos
- Si N > 1 entonces todos los 0 a la derecha son significativos
- Si N < 1 entonces solo los 0 al final y entre CS son significativos

## Análisis de errores
El término error puede definirse como la inexactitud y/o imprecisión en las predicciones, en el supuesto de que conozcamos el valor verdadero al que queremos llegar los errores pueden definirse de la siguiente manera.
- Error absoluto: ![equation](https://latex.codecogs.com/svg.image?e&space;=&space;\left|&space;\widetilde{p}&space;-&space;p&space;\right|) 
- Error relativo: ![equation](https://latex.codecogs.com/svg.image?e&space;=&space;\left|&space;\frac{&space;\widetilde{p}&space;-&space;p&space;}{p}&space;\right|)
- Error porcentual: ![equation](https://latex.codecogs.com/svg.image?e&space;=&space;\left|&space;\frac{&space;\widetilde{p}&space;-&space;p&space;}{p}&space;\right|&space;\cdot&space;100)

donde ![equation](https://latex.codecogs.com/svg.image?\widetilde{p})  es una aproximación del valor real
## Análisis de errores en métodos iterativos
En los métodos iterativos siempre vamos a hacer el supuesto de que el valor obtenido en la siguiente ejecución será una mejor aproximación al valor real.
- Error absoluto: ![equation](https://latex.codecogs.com/svg.image?e&space;=&space;\left|&space;\widetilde{p}_{n&plus;1}&space;-&space;p_{n}&space;\right|)
- Error relativo: ![equation](https://latex.codecogs.com/svg.image?e&space;=&space;\left|&space;\frac{\widetilde{p}_{n&plus;1}&space;-&space;p_{n}}{\widetilde{p}_{n&plus;1}}&space;\right|)

### Criterio de parada
Una de las preguntas que surge cuando se emplean métodos iterativos, es: **¿Cuándo es suficiente una aproximación?** En ese sentido, siempre dependerá del contexto del problema. Sin embargo, nosotros definiremos un criterio conservador para obtener tantas cifras significativas.
En este caso diremos que **p** es una mejor aproximación a **p** con **d** cifras significativas, si **d** es el mayor número natural que verifique 


![equation](https://latex.codecogs.com/svg.image?E_{r}&space;=&space;\frac{\left|&space;\widetilde{p}&space;-&space;p&space;\right|}{\left|&space;\widetilde{p}&space;\right|}&space;\leq&space;0.5&space;\cdot&space;10^{-d})

## Métodos cerrados
Son aquellos métodos que aprovechan el hecho de que una función cambia de signo en la vecindad de una raíz. A estas técnicas se les llama métodos cerrados, o de intervalos, porque se necesita de dos valores iniciales para la raíz. Como su nombre lo indica, dichos valores iniciales deben “encerrar”, o estar a ambos lados de la raíz.

<img src="https://i.imgur.com/E8sAHFA.png" alt="image" style="width:200px;height:200px;">

### Método de bisección
El método de bisección es un método numérico utilizado para encontrar la raíz de una función en un intervalo dado. El método se basa en el teorema de Bolzano, que establece que si una función es continua en un intervalo y los valores de la función en los extremos del intervalo tienen signos opuestos, entonces existe al menos una raíz en ese intervalo.

#### Criterio de parada
El error en el k-ésimo paso estará dado por la expresión 

![equation](https://latex.codecogs.com/svg.image?E_{relativo}&space;=&space;\frac{\left|&space;b_{original}&space;-&space;a_{original}&space;\right|}{2^{k}})

#### Predicción de bisecciones
Una de las ventajas de este método es que es posible predecir la cantidad de bisecciones a realizar para llegar a una determinada precisión mediante la fórmula

![equation](https://latex.codecogs.com/svg.image?k&space;=&space;\left&space;[&space;\frac{ln(b&space;-&space;a)&space;-&space;ln(\alpha&space;)}{ln(2)}&space;\right&space;]) 

Donde ![equation](https://latex.codecogs.com/svg.image?\alpha) es la tolerancia

#### Algoritmo
1. Aseguramos que la función f(x) sea continua en el intervalo [a, b]
2. Comprobamos que f(a) * f(b) < 0
3. Calculamos el punto medio "m" del intervalo [a, b]
4. El punto "m" debe evaluarse en la función, si el valor es cero significa que hallamos la raíz por el contrario, se redefine el intervalo [a, b] como [m, b] o [a, m] según se haya determinado en cuál de estos intervalos ocurre el cambio de signo.
5. Con este nuevo intervalo se continúa de manera sucesiva hasta "encerrar" la solución en un intervalo cada vez más pequeño, hasta alcanzar la precisión deseada.

#### Desarrollo en Python
Para la función  ![equation](https://latex.codecogs.com/svg.image?&space;f(x)&space;=&space;x^{2}&space;-&space;cos(x)&space;-&space;1)  en el intervalo [1, 2] con una precisión de cuatro cifras significativas

```python
import matplotlib.pyplot as plt
import numpy as np

def main():
    # Definimos la función para la cual queremos aproximar la raíz
    def f(x):
        return x**2 - np.cos(x) - 1
    
    # Establecemos el intervalo de la función
    a = 1
    b = 2

    # Establecemos el criterio de parada
    def cifras_significativas(d):
        return (1/2) * (10**-d)

    # Estimamos la cantidad de bisecciones necesarias para aproximarse al resultado con tantas cifras significativas.
    def prediccion_de_bisecciones():
        return np.ceil((np.log(b-a) - np.log(cifras_significativas(4)))/np.log(2))
    
    # Comprobamos el teorema de bolzano en el intervalo
    if f(a) * f(b) < 0:
        print('Para aproximarse a la raiz con una tolerancia de ', cifras_significativas(4), ' se necesitaran ', prediccion_de_bisecciones(), ' bisecciones')
        biseccion = 1
        a_original = a
        b_original = b

        while True:
            # Definimos el punto medio del intervalo y el error.
            m = (a + b) / 2 
            error = (b_original - a_original)/2**biseccion

            # Si la función evaluada en a tiene el mismo signo que la función evaluada en m, entonces cambiamos a por m.        
            if f(a) * f(m) >= 0:
                a = m
            
            # Si la función evaluada en b tiene el mismo signo que la función evaluada en m, entonces cambiamos b por m.
            if f(b) * f(m) >= 0:
                b = m

            # Establecemos el criterio de parada
            if(error < cifras_significativas(4)):
                print("La raiz de la funcion es: ", m)
                break

            biseccion += 1
    else:
        print('El intervalo seleccionado no verifica el teorema de Bolzano')

if __name__ == '__main__':
    main()
```

### Método de Regula Falsi
La falsa posición es una alternativa basada en una visualización gráfica. El hecho de que se reemplace la curva por una línea recta da una “falsa posición” de la raíz; de aquí el nombre de método de la falsa posición, o en latín, regula falsi. También se le conoce como método de interpolación lineal.

Mejora la convergencia del Método de Bisección, considerando no solo el signo de la función en los extremos del intervalo, sino que aprovecha los valores de la imagen. Determina una recta que une los puntos (a, f(a)) y (b, f(b)) y fija el nuevo extremo c en la intersección de dicha recta con el eje x.

Vamos a definir el punto "c" como:

![equation](https://latex.codecogs.com/svg.image?c&space;=&space;\frac{a&space;\cdot&space;f(b)&space;-&space;b&space;\cdot&space;f(a)}{f(b)&space;-&space;f(a)})

#### Criterio de parada
Para calcular el error utilizaremos la siguiente expresión

![equation](https://latex.codecogs.com/svg.image?E_{relativo}&space;=&space;\left|&space;{c_{nuevo}&space;-&space;c_{actual}}&space;\right|&space;<&space;\alpha&space;)

Donde ![equation](https://latex.codecogs.com/svg.image?\alpha) es la tolerancia

#### Algoritmo
1. Aseguramos que la función f(x) sea continua en el intervalo [a, b]
2. Comprobamos que f(a) * f(b) < 0
3. Calculamos el punto "c" del intervalo [a, b]
4. El punto "c" debe evaluarse en la función, si el valor es cero significa que hallamos la raíz por el contrario, se redefine el intervalo [a, b] como [c, b] o [a, c] según se haya determinado en cuál de estos intervalos ocurre el cambio de signo.
5. Con este nuevo intervalo se continúa de manera sucesiva hasta "encerrar" la solución en un intervalo cada vez más pequeño, hasta alcanzar la precisión deseada.

#### Desarrollo en Python
Para la función  ![equation](https://latex.codecogs.com/svg.image?f(x)&space;=&space;x&space;\cdot&space;sen(x)&space;-&space;1)  en el intervalo [0, 2] con una precisión de cuatro cifras significativas

```
import matplotlib.pyplot as plt
import numpy as np

def main():
    # Definimos la función para la cual queremos aproximar la raíz
    def f(x):
        return x * np.sin(x) - 1
    
    # Establecemos el intervalo de la función
    a = 0
    b = 2

    # Establecemos el criterio de parada
    def cifras_significativas(d):
        return (1/2) * (10**-d)
    
    # Calculamos el punto "c"
    def calcular_c(a, b):
        return (a * f(b) - b * f(a))/(f(b) - f(a))
    
    # Comprobamos el teorema de bolzano en el intervalo
    if f(a) * f(b) < 0:
        c_actual = calcular_c(a, b)
        while True:
            # Si la función evaluada en a tiene el mismo signo que la función evaluada en c, entonces cambiamos a por c.        
            if f(a) * f(c_actual) >= 0:
                a = c_actual
            
            # Si la función evaluada en b tiene el mismo signo que la función evaluada en c, entonces cambiamos b por c.
            if f(b) * f(c_actual) >= 0:
                b = c_actual

            # Definimos el punto "c" nuevo del intervalo, el error y ahora ese c pasará a ser el actual.
            c_nuevo = calcular_c(a, b)
            error = np.abs(c_nuevo - c_actual)/c_nuevo
            c_actual = c_nuevo

            # Establecemos el criterio de parada
            if(error < cifras_significativas(4)):
                print("La raiz de la funcion es: ", c_actual)
                break
    else:
        print('El intervalo seleccionado no verifica el teorema de Bolzano')

if __name__ == '__main__':
    main()
```

## Métodos abiertos
Son aquellos métodos que  se basan en fórmulas que requieren únicamente de un solo valor de inicio x o que empiecen con un par de ellos, pero que no necesariamente encierran la raíz. Éstos, algunas veces divergen o se alejan de la raíz verdadera a medida que se avanza en el cálculo. Sin embargo, cuando los métodos abiertos convergen, en general lo hacen mucho más rápido que los métodos cerrados.

<img src="https://i.imgur.com/WdI6bqf.png" alt="image" style="width:200px;height:200px;">

### Iteración del punto fijo
El método de iteración del punto fijo implica tomar un valor inicial y aplicar repetidamente una fórmula o función específica a ese valor para acercarse cada vez más a la solución deseada.

- Sea g: [a,b] -> R continuamente derivable, tal que g(x) pertenece a [a,b] para toda x perteneciente a [a,b]. Entonces, g tiene un punto fijo x* en [a,b]
- Si g'(x) existe en [a,b] y existe una constante positiva k < 1 con |g′(x)| ≤ k, para toda x perteneciente (a,b); entonces el punto fijo x* en [a,b] es único.
- Además, se puede acortar el error de la iteración n-ésima por (Para N > 2):


![equation](https://latex.codecogs.com/svg.image?\left|&space;x_{n}&space;-&space;x^{*}&space;\right|&space;\leq&space;\frac{k^{n}}{1&space;-&space;k}&space;\cdot&space;\left|&space;x_{1}&space;-&space;x_{2}\right|)


### Comportamiento
En la práctica, si la derivada de g es continua, sucede que:
- Si: |g’(x)| > 1 entonces los iterados no convergen a x*
- Si: |g’(x)| < 1 entonces los iterados no convergen linealmente a x*
- Si: |g’(x)| = 1 entonces los iterados convergen cuadráticamente a x*

### Algoritmo
1. Hacer de f(x) = 0 a x = g(x) mediante un desarrollo algebraico. Esta ecuación se puede “acomodar” de varias maneras por lo tanto vamos a tener varios x = g(x).
2. Derivar las g(x) y evaluar en todas, la semilla. Para obtener una semilla se puede resolver la desigualdad −1 ≤ g′(x) ≤ 1. Analizar la convergencia según la tabla anterior. También se puede analizar el gráfico y ver el cambio de signo de la función
3. Establecer un criterio de parada




## Bibliografía
- Chapra, S. C., & Canale, R. P. (2010). Métodos numéricos para ingenieros (5a ed.). México: McGrawHill.