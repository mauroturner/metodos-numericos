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

```python
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

### Iteración de punto fijo
El método de iteración de punto fijo implica tomar un valor inicial y aplicar repetidamente una fórmula o función específica a ese valor para acercarse cada vez más a la solución deseada.

- Sea g: [a,b] -> R continuamente derivable, tal que g(x) pertenece a [a,b] para toda x perteneciente a [a,b]. Entonces, g tiene un punto fijo x* en [a,b]
- Si g'(x) existe en [a,b] y existe una constante positiva k < 1 con |g′(x)| ≤ k, para toda x perteneciente (a,b); entonces el punto fijo x* en [a,b] es único.
- Además, se puede acortar el error de la iteración n-ésima por (Para N > 2):


![equation](https://latex.codecogs.com/svg.image?\left|&space;x_{n}&space;-&space;x^{*}&space;\right|&space;\leq&space;\frac{k^{n}}{1&space;-&space;k}&space;\cdot&space;\left|&space;x_{1}&space;-&space;x_{2}\right|)


#### Comportamiento
En la práctica, si la derivada de g es continua, sucede que:
- Si: |g’(x)| > 1 entonces los iterados no convergen a x*
- Si: |g’(x)| < 1 entonces los iterados no convergen linealmente a x*
- Si: |g’(x)| = 1 entonces los iterados convergen cuadráticamente a x*

#### Algoritmo
1. Hacer de f(x) = 0 a x = g(x) mediante un desarrollo algebraico. Esta ecuación se puede “acomodar” de varias maneras por lo tanto vamos a tener varios x = g(x).
2. Derivar las g(x) y evaluar en todas, la semilla. Para obtener una semilla se puede resolver la desigualdad −1 ≤ g′(x) ≤ 1. Analizar la convergencia según la tabla anterior. También se puede analizar el gráfico y ver el cambio de signo de la función
3. Establecer un criterio de parada

#### Desarrollo en Python
Para la función ![equation](https://latex.codecogs.com/svg.image?&space;f(x)=e^x-4&plus;x&space;) con una raíz en [1, 2] con una precisión de ![equation](https://latex.codecogs.com/svg.image?\varepsilon_r<10^-2)

```python
import numpy as np

def main():
    # Definimos la función para la cual queremos aproximar la raíz
    def f(x):
        return (np.exp(1) ** x) - 4 + x
    
    # Convertimos f(x) a x = g(x)
    # Opción 1
    def g(x):
        return 4 - (np.exp(1) ** x)
    
    # Opción 2
    def h(x):
        return (np.exp(1) ** x) - 4 + 2 * x
    
    # Opción 3
    def j(x):
        return np.log(4 - x)
    
    # Establecemos el intervalo de la función
    a = 1
    b = 2

    # Establecemos el criterio de parada
    def cifras_significativas(d):
        return (1/2) * (10**-d)
    
    def punto_fijo(funcion, x0, tolerancia, max_iter):
        x = x0
        iteraciones = 0
        
        while iteraciones < max_iter:
            x_nueva = funcion(x)
            
            # Verificamos el criterio de parada
            if np.abs(x_nueva - x) < tolerancia:
                return x_nueva, iteraciones
            
            x = x_nueva
            iteraciones += 1
        
        raise ValueError('El método no converge en el número máximo de iteraciones.')
    
    # Aplicamos el método de punto fijo a la función j(x)
    x0 = 1
    tolerancia = cifras_significativas(2)
    max_iter = 10
    
    try:
        raiz, iteraciones = punto_fijo(j, x0, tolerancia, max_iter)
        print(f"Raíz: {raiz}")
        print(f"Número de iteraciones: {iteraciones}")
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()
```

### Método de Newton - Raphson
Esta técnica es una versión mejorada del método del punto fijo y es bastante popular. Se destaca por avanzar más rápido hacia la raíz, a veces duplicando la cantidad de dígitos exactos en cada intento, siempre y cuando se cumplan ciertas condiciones.

Hablando de manera sencilla, partiendo de una estimación Xn​, para la siguiente aproximación Xn+1​, simplemente seguimos la tangente de la curva hasta que cruza el eje x en el punto (Xn, Xn+1). 

#### Algoritmo
1. Seleccionar un punto inicial x0​ cerca de la raíz.
2. En cada iteración, calcula el valor Xn+1 con la fórmula:
![equation](https://latex.codecogs.com/svg.image?&space;x_{nueva}=x_{anterior}-\frac{f(x_{anterior})}{f'(x_{anterior})})

#### Desarrollo en Python
Para la función ![equation](https://latex.codecogs.com/svg.image?x^2-cos(x)-1) con una raíz en [1, 2] con una precisión de ![equation](https://latex.codecogs.com/svg.image?\varepsilon_r<10^-5)

```python
import numpy as np

def main():
    # Definimos la función para la cual queremos aproximar la raíz
    def f(x):
        return (np.exp(1) ** x) - 4 + x
    
    # Convertimos f(x) a x = g(x)
    # Opción 1
    def g(x):
        return 4 - (np.exp(1) ** x)
    
    # Opción 2
    def h(x):
        return (np.exp(1) ** x) - 4 + 2 * x
    
    # Opción 3
    def j(x):
        return np.log(4 - x)
    
    # Establecemos el intervalo de la función
    a = 1
    b = 2

    # Establecemos el criterio de parada
    def cifras_significativas(d):
        return (1/2) * (10**-d)
    
    def punto_fijo(funcion, x0, tolerancia, max_iter):
        x = x0
        iteraciones = 0
        
        while iteraciones < max_iter:
            x_nueva = funcion(x)
            
            # Verificamos el criterio de parada
            if np.abs(x_nueva - x) < tolerancia:
                return x_nueva, iteraciones
            
            x = x_nueva
            iteraciones += 1
        
        raise ValueError('El método no converge en el número máximo de iteraciones.')
    
    # Aplicamos el método de punto fijo a la función j(x)
    x0 = 1
    tolerancia = cifras_significativas(2)
    max_iter = 10
    
    try:
        raiz, iteraciones = punto_fijo(j, x0, tolerancia, max_iter)
        print(f"Raíz: {raiz}")
        print(f"Número de iteraciones: {iteraciones}")
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()
```

### Método de la secante
Hay funciones cuyas derivadas son un verdadero dolor de cabeza para calcular, ahí es donde entra en juego este método (¡No se necesita calcular derivadas!). 

Este método necesita dos valores iniciales de x. Sin embargo, no es necesario que la función f(x) cambie de signo entre esos dos valores. Por eso, no lo llamamos un método cerrado.

#### Algoritmo
1. Seleccionar dos valores iniciales x0​ y x1​ que estén cerca de la raíz.
2. Evaluar la función en f(x0) y f(x1)
3. Calcular la pendiente m con

![equation](https://latex.codecogs.com/svg.image?\frac{f(x_1)-f(x_0)}{x_1-x_0})

4. Calcular el nuevo valor de x con la fórmula:

![equation](https://latex.codecogs.com/svg.image?x_{nueva}=x_{1}-\frac{f(x_{1})}{m})

#### Desarrollo en Python
Para la función ![equation](https://latex.codecogs.com/svg.image?x^2-cos(x)-1) con una raíz en [-1, -2] con una precisión de ![equation](https://latex.codecogs.com/svg.image?\varepsilon_r<10^-5)

```python
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
```

## Dos métodos especiales
Además de los métodos que hemos programado en el repositorio, existen otras dos alternativas especiales para hallar las raíces de un polinomio, estos son:

- El método de Müller
- El método de Bairstow


### Método de Müller
El método de Muller es un método numérico que se asemeja al método de la secante, que aproxima una raíz mediante una línea recta trazada entre dos puntos. En el caso del método de Muller, en lugar de utilizar dos puntos, se emplean tres puntos para construir una parábola. 
La parábola se ajusta de manera que pase por los tres puntos iniciales, y se determinan los coeficientes de la parábola.

<img src="https://i.imgur.com/Rzq3Fy7.jpg" alt="image" style="width:100%;height:100%;">

#### Algoritmo
1. Evaluar la función en tres puntos cercanos a la raíz 
2. Calcular los siguientes valores

![equation](https://latex.codecogs.com/svg.image?h_{0}=x_{1}-x_{0})

![equation](https://latex.codecogs.com/svg.image?h_{1}=x_{12}-x_{1})

![equation](https://latex.codecogs.com/svg.image?d_0=\frac{f(x_1)-f(x_0)}{h_0})

![equation](https://latex.codecogs.com/svg.image?d_1=\frac{f(x_2)-f(x_1)}{h_1})

![equation](https://latex.codecogs.com/svg.image?d=\frac{d_1-d_0}{h_0&plus;h_1)

![equation](https://latex.codecogs.com/svg.image?b=d\cdot&space;h1&plus;d_1)

![equation](https://latex.codecogs.com/svg.image?D=\sqrt{b^2-4\cdot&space;f(x_2)\cdot&space;d})


3. Realizar las siguientes comparaciones

Si | b - D | < | b + D |, entonces: E = b + D

Si | b - D | > | b + D |, entonces: E = b - D

4. Calcular h, x3 y la tolerancia

![equation](https://latex.codecogs.com/svg.image?h=\frac{-2\cdot&space;f(x_2)}{E})

![equation](https://latex.codecogs.com/svg.image?x_3=x_2&plus;h)

![equation](https://latex.codecogs.com/svg.image?\left|h\right|)

5. Realizar la siguiente iteración con

x3 -> x2

x2 -> x1

x1 -> x0

#### Desarrollo en Python
Para la función ![equation](https://latex.codecogs.com/svg.image?&space;x^3-13x-12) con los valores iniciales x0, x1 y x2 = 4,5; 5,5 y 5 con una precisión de ![equation](https://latex.codecogs.com/svg.image?\varepsilon_r<10^-5)

```Python
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
```

### Método de Bairstow
El Método de Bairstow es un algoritmo iterativo utilizado para encontrar las raíces de polinomios de segundo o mayor grado. Este método es especialmente eficiente para polinomios con coeficientes reales y complejos.
La idea principal detrás del Método de Bairstow es realizar una factorización cuadrática sucesiva del polinomio original, reduciéndolo gradualmente hasta que se obtengan las raíces finales. Se inicia con una suposición de las raíces y luego se ajustan iterativamente para obtener una mejor aproximación.

#### Algoritmo

1. Se tiene una ecuación de la forma ![equation](https://latex.codecogs.com/svg.image?f_{n}(x)=a_0&plus;a_1x&plus;a_2x^{2}&plus;...&plus;a_nx^n)

2. Se divide entre el factor x - t, residuo R = B0

3. Se calculan los coeficientes

![equation](https://latex.codecogs.com/svg.image?b_n=a_n&space;)

![equation](https://latex.codecogs.com/svg.image?b_{n-1}=a_{n-1}&plus;rb_{n})

![equation](https://latex.codecogs.com/svg.image?b_{i}=a_{i}&plus;rb_{i&plus;1}&plus;sb_{i&plus;2}) para i = n - 2 a 0

![equation](https://latex.codecogs.com/svg.image?c_n=b_n)

![equation](https://latex.codecogs.com/svg.image?c_{n-1}=b_{n-1}&plus;rc_n)

![equation](https://latex.codecogs.com/svg.image?c_{i}=b_{i}&plus;rc_{i&plus;1}&plus;sc_{i&plus;2}) para i = n - 2 a 1

4. Se reemplazan estos datos en las ecuaciones

![equation](https://latex.codecogs.com/svg.image?c_2\Delta&space;r&plus;c_3\Delta&space;s=-b_1)

![equation](https://latex.codecogs.com/svg.image?c_1\Delta&space;r&plus;c_2\Delta&space;s=-b_0)

5. Despejando r y s

![equation](https://latex.codecogs.com/svg.image?\Delta&space;r=\frac{c_3&space;b_0-c_2&space;b_1}{c_2^2-c_1&space;c_3})

![equation](https://latex.codecogs.com/svg.image?\Delta&space;s=\frac{c_1&space;b_1-c_2&space;b_0}{c_2^2-c_1&space;c_3})

6. Se corrigen los nuevos valores de r y s

7. Se evalúa el erorr aproximado

8. Se obtienen los valores de las raíces

![equation](https://latex.codecogs.com/svg.image?x=\frac{r\pm\sqrt{r^2&plus;4s}}{2})

#### Desarrollo en Python
Para la función  ![equation](https://latex.codecogs.com/svg.image?&space;x^5-3.5x^4&plus;2.75x^3&plus;2.125x^2-3.875x&plus;1.25) utilizando los valores r = s = -1 iterando hasta e = 1%

```Python
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
```

## Sistema de ecuaciones lineales
Los sistemas de ecuaciones lineales son conjuntos de ecuaciones en las que cada ecuación es una función lineal de las mismas variables. Estos sistemas se puede representar de la siguiente manera:

<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/4e7a71b074b0bd4839735fb1a3a6990ef81f91d2" alt="image">

donde x1, x2, …, xn​ son las variables desconocidas, Aij​ son los coeficientes constantes, y Bi​ son los términos constantes en cada ecuación. Este sistema tiene m ecuaciones y n variables. Estos sistemas se pueden resolver para encontrar los valores de las variables desconocidas que satisfacen todas las ecuaciones simultáneamente.

## Matrices
Un sistema de ecuaciones lineales se puede representar de manera matricial, lo que facilita su análisis y resolución. Por ejemplo, el siguiente sistema de ecuaciones lineales con dos incógnitas, x e y:

<img src="https://latex.codecogs.com/svg.image?\left\{\begin{matrix}a_{11}x&a_{12}y&=&b_{1}\\a_{21}x&a_{22}y&=&b_{2}\\\end{matrix}\right." alt="image">

Se puede representar en forma matricial definiendo la matriz de coeficientes A, el vector de incógnitas X, y el vector de términos constantes B de la siguiente manera:

<img src="https://latex.codecogs.com/svg.image?A=\begin{pmatrix}a_{11}&b_{12}\\a_{21}&b_{22}\\\end{pmatrix}" alt="image">

<img src="https://latex.codecogs.com/svg.image?X=\begin{pmatrix}x\\y\end{pmatrix}" alt="image">

<img src="https://latex.codecogs.com/svg.image?B=\begin{pmatrix}b_{1}\\b_{2}\end{pmatrix}" alt="image">

Entonces, el sistema de ecuaciones se puede expresar de forma compacta como 

<img src="https://latex.codecogs.com/svg.image?A\cdot&space;X=B" alt="image">

Por lo tanto, la solución del sistema se encuentra multiplicando ambos lados de la ecuación por la inversa de la matriz A

<img src="https://latex.codecogs.com/svg.image?X=A^{-1}\cdot&space;B&space;" alt="image">

### Operaciones matriciales
completar

### Tipos especiales de matrices cuadradas
Hay diferentes formas especiales de matrices cuadradas que son importantes y que deben mencionarse

#### Matriz simétrica
Es aquella donde 

![equation](https://latex.codecogs.com/svg.image?&space;a_{ij}=a_{ji}) 

para todo i y j. Por ejemplo:

<img src="https://latex.codecogs.com/svg.image?\left[A\right]=\begin{pmatrix}5&1&2\\1&3&7\\2&7&8\\\end{pmatrix}" alt="image">

#### Matriz diagonal
Una matriz diagonal es una matriz cuadrada donde todos los elementos fuera de la diagonal principal son iguales a cero

<img src="https://latex.codecogs.com/svg.image?\left[A\right]=\begin{pmatrix}a_{11}&&&\\&a_{22}&&\\&&a_{33}&\\&&&a_{44}\\\end{pmatrix}" alt="image">

#### Matriz identidad
Una matriz identidad es una matriz diagonal donde todos los elementos sobre la diagonal principal son iguales a 1

<img src="https://latex.codecogs.com/svg.image?\left[I\right]=\begin{pmatrix}1&&&\\&1&&\\&&1&\\&&&1\\\end{pmatrix}" alt="image">

#### Matriz triangular superior
Es aquella donde todos los elementos por debajo de la diagonal principal son cero

<img src="https://latex.codecogs.com/svg.image?\left[A\right]=\begin{pmatrix}a_{11}&a_{12}&a_{13}&a_{14}\\&a_{22}&a_{23}&a_{24}\\&&a_{33}&a_{34}\\&&&a_{44}\\\end{pmatrix}" alt="image">

#### Matriz triangular inferior
Es aquella donde todos los elementos por arriba de la diagonal principal son cero

<img src="https://latex.codecogs.com/svg.image?\left[A\right]=\begin{pmatrix}a_{11}&&&\\a_{21}&a_{22}&&\\a_{31}&a_{32}&a_{33}&\\a_{41}&a_{42}&a_{43}&a_{44}\\\end{pmatrix}" alt="image">

#### Matriz bandeada
Es aquella que tiene todos los elementos iguales a cero, con la excepción de una banda centrada sobre la diagonal principal

<img src="https://latex.codecogs.com/svg.image?\left[A\right]=\begin{pmatrix}a_{11}&a_{12}&&\\a_{21}&a_{22}&a_{23}&\\&a_{32}&a_{33}&a_{34}\\&&a_{43}&a_{44}\\\end{pmatrix}" alt="image">

### Normas vectoriales
Una norma vectorial es una función que asigna a cada vector en un espacio vectorial un número real no negativo. La norma de un vector v, generalmente denotada como ∥v∥, satisface algunas propiedades específicas, como la homogeneidad positiva, la desigualdad triangular y la identidad del triángulo

#### Norma valor absoluto
Suponiendo el vector V = (1; 3; -5; 2)

![equation](https://latex.codecogs.com/svg.image?\left\|x\right\|_{1}=\sum_{i=1}^{n}\left|x_{i}\right|=1&plus;3&plus;5&plus;2=11) 

#### Norma euclidea
Suponiendo el vector V = (1; 3; -5; 2)

![equation](https://latex.codecogs.com/svg.image?\left\|x\right\|_{2}=\sqrt{\left(\sum_{i=1}^{n}x_{i}^2\right)}=\sqrt{1^2&plus;3^2&plus;5^2&plus;2^2}=\sqrt{39}) 

#### Norma máxima o infinita
Suponiendo el vector V = (1; 3; -5; 2)

![equation](https://latex.codecogs.com/svg.image?\left\|x\right\|_{\infty}=max\left|x_{i}\right|i=1,...,n=max\begin{Bmatrix}1;3;-5;2\end{Bmatrix}=5) 

### Normas matriciales
Al igual que con los vectores, las matrices también pueden tener asociadas diversas normas que miden de alguna manera su tamaño o magnitud

#### Norma fila o infinito
Teniendo en cuenta la matriz 

<img src="https://latex.codecogs.com/svg.image?A=\begin{pmatrix}1&2&3\\4&5&0\\-1&2&-3\\\end{pmatrix}" alt="image">

<img src="https://imgur.com/735aowG.png" alt="image">

#### Norma columna
<img src="https://latex.codecogs.com/svg.image?A=\begin{pmatrix}1&2&3\\4&5&0\\-1&2&-3\\\end{pmatrix}" alt="image">

<img src="https://imgur.com/0x2YAh9.png" alt="image">

#### Norma Frobenius
<img src="https://latex.codecogs.com/svg.image?A=\begin{pmatrix}1&2&3\\4&5&0\\-1&2&-3\\\end{pmatrix}" alt="image">

<img src="https://imgur.com/IeZYhQA.png" alt="image">

## Métodos directos
Los métodos directos para resolver sistemas de ecuaciones lineales (SEL) son algoritmos que encuentran la solución exacta del sistema en un número finito de pasos. Estos métodos proporcionan una solución única y no requieren una suposición inicial, los métodos más comunes son:

* Sustitución
* Reducción
* Igualación
* Método de Gauss
* Método de Gauss - Jordan
* Regla de Cramer
* Método de la matriz inversa

Estos métodos son eficientes para sistemas de ecuaciones lineales de tamaño pequeño o moderado y son especialmente útiles cuando se necesita una solución exacta. Sin embargo, la complejidad computacional de estos métodos puede aumentar significativamente con el tamaño del sistema.
En este caso, optaremos por no enfocarnos en los métodos directos para la resolución de sistemas de ecuaciones lineales. En lugar de eso, dirigiremos nuestra atención hacia los métodos indirectos o iterativos.

## Métodos indirectos
Los métodos indirectos, también conocidos como métodos iterativos, son técnicas utilizadas para resolver problemas matemáticos mediante la repetición de un proceso de aproximación sucesiva. A diferencia de los métodos directos, que buscan obtener una solución exacta en un número finito de pasos, los métodos iterativos mejoran continuamente la aproximación a la solución mediante la repetición de un conjunto de operaciones.
En este contexto, centraremos nuestra atención en dos métodos iterativos ampliamente utilizados para resolver sistemas de ecuaciones lineales: el Método de Jacobi y el Método de Gauss-Seidel. 

### Método de Jacobi
Este método es particularmente útil cuando se trata de sistemas lineales de gran tamaño. Desarrollado por el matemático alemán Carl Gustav Jacob Jacobi, este método aborda la resolución de sistemas de ecuaciones al descomponer la matriz de coeficientes en la suma de una matriz diagonal y dos matrices triangulares. 

#### Algoritmo 
Es decir: la matriz A es la suma de tres matrices: una matriz diagonal D, y dos matrices triangulares L y U. La descomposición se expresa como A = D + L + U, donde:

* D es la matriz diagonal que contiene los elementos diagonales de A
* L es la matriz triangular inferior con los elementos fuera de la diagonal de A
* U es la matriz triangular superior con los elementos fuera de la diagonal de A

Entonces:

1. Se distribuye x

![equation](https://latex.codecogs.com/svg.image?(L&plus;D&plus;U)\cdot&space;x=b)  

2. Se despeja x y se utiliza por conveniencia a la diagonal

![equation](https://latex.codecogs.com/svg.image?Lx&plus;Dx&plus;Ux=b) 

3. Se multiplica por la inversa de la diagonal

![equation](https://latex.codecogs.com/svg.image?Dx=(-L-U)x&plus;b) 

![equation](https://latex.codecogs.com/svg.image?x=D^{-1}(-L-U)x&plus;D^{-1}&plus;b) 

5. Se renombran las variables

![equation](https://latex.codecogs.com/svg.image?T=D^{-1}(-L-U)) 

![equation](https://latex.codecogs.com/svg.image?C=D^{-1}b) 

6. Por lo tanto

![equation](https://latex.codecogs.com/svg.image?x=Tx&plus;C) 

#### Desarrollo en Python
```python
import numpy as np

def main():
    # Definimos el sistema de ecuaciones
    A = np.array([[3, -1, -1],
                  [-1, 3, 1],
                  [2, 1, 4]])

    b = np.array([1, 3, 7])

    # Establecemos el criterio de parada (norma infinito en este caso)
    def criterio_parada(x, x_prev, tolerancia):
        return np.linalg.norm(x - x_prev, np.inf) < tolerancia

    def metodo_jacobi(A, b, x0, tolerancia, max_iter):
        n = len(b)
        x = x0.copy()
        x_prev = x0.copy()
        iteraciones = 0

        while iteraciones < max_iter:
            for i in range(n):
                sigma = np.dot(A[i, :n], x_prev[:n]) + np.dot(A[i, n:], x_prev[n:])
                x[i] = (b[i] - sigma + A[i, i] * x_prev[i]) / A[i, i]

            # Verificamos el criterio de parada
            if criterio_parada(x, x_prev, tolerancia):
                return x, iteraciones

            x_prev = x.copy()
            iteraciones += 1

        raise ValueError("El método no converge en el número máximo de iteraciones.")

    # Aplicamos el método de Jacobi al sistema de ecuaciones
    x0 = np.zeros_like(b, dtype=float)
    try:
        solucion, iteraciones = metodo_jacobi(A, b, x0, 0.000001, 100)
        print("Solución encontrada:")
        print(solucion)
        print(f"Iteraciones: {iteraciones}")
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()

```

### Método de Gauss - Seidel
El método de Gauss-Seidel es un algoritmo iterativo utilizado para resolver sistemas de ecuaciones lineales. Este método lleva el nombre de los matemáticos Carl Friedrich Gauss y Philipp Ludwig von Seidel. A diferencia del método de Jacobi, el método de Gauss - Seidel actualiza las soluciones de las ecuaciones en el mismo orden en el que aparecen en el sistema.

La idea principal del método de Gauss-Seidel es realizar actualizaciones sucesivas de las soluciones de las ecuaciones, utilizando los valores más recientes disponibles. En cada iteración, las nuevas soluciones se utilizan de inmediato en las siguientes ecuaciones del sistema, lo que puede conducir a una convergencia más rápida en comparación con el método de Jacobi.

Este método es particularmente eficaz para sistemas en los que la matriz de coeficientes es diagonalmente dominante o simétrica y definida positiva, además de esta forma se garantiza la convergencia. No obstante, el método puede funcionar, aunque no se satisfagan estos criterios.

#### Algoritmo

1. Si los elementos de la diagonal no son todos cero, la primera ecuación se puede resolver para x1, la segunda para x2 y la tercera para x3, para obtener:

![equation](https://latex.codecogs.com/svg.image?x_{1}=\frac{b_{1}-a_{12}x_{2}-a_{13}x_{3}}{a_{11}}) 

![equation](https://latex.codecogs.com/svg.image?x_{2}=\frac{b_{2}-a_{21}x_{1}-a_{23}x_{3}}{a_{22}}) 

![equation](https://latex.codecogs.com/svg.image?x_{3}=\frac{b_{3}-a_{31}x_{1}-a_{32}x_{2}}{a_{33}}) 

2. Se puede empezar el proceso de solución al escoger valores iniciales para las x. Una forma simple para obtener los valores iniciales es suponer que todos son cero, estos se sustituyen en la ecuación:

![equation](https://latex.codecogs.com/svg.image?x_{1}=\frac{b_{1}-a_{12}x_{2}-a_{13}x_{3}}{a_{11}}) 

3. Con el valor obtenido para X1, se sustituye junto con el valor previo cero de x3 en la ecuación

![equation](https://latex.codecogs.com/svg.image?x_{2}=\frac{b_{2}-a_{21}x_{1}-a_{23}x_{3}}{a_{22}}) 

4. Se calcula el nuevo valor de X2, y se repite el proceso con la ecuación para calcular un nuevo valor de X3.

![equation](https://latex.codecogs.com/svg.image?x_{3}=\frac{b_{3}-a_{31}x_{1}-a_{32}x_{2}}{a_{33}}) 

5. Luego se regresa a la primera ecuación y se repite  todo el procedimiento hasta que la solución converja suficientemente cerca a los valores verdaderos.

#### Desarrollo en Python
```python
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
```

## Integración numérica

La integración numérica es una herramienta que se utiliza para obtener valores aproximados de integrales definidas que no pueden calcularse analíticamente. El objetivo es aproximar la integral definida de una función 𝑓(x) en un intervalo [a, b] evaluando 𝑓(x) en un número finito de puntos.

### Cuadratura numérica
En esta sección se estudian técnicas para la aproximación de integrales cuyas primitivas no siempre pueden calcularse aplicando el teorema fundamental del cálculo, especialmente sobre funciones que no tienen primitiva elemental. El método básico para resolver este tipo de integrales se conoce como cuadratura numérica.

![equation](https://latex.codecogs.com/svg.image?\int_{a}^{b}f(x)d(x)=\sum_{i=1}^{n}w_{i}\cdot&space;f(x_{i})&plus;E(f^{(n)}))

<img src="https://i.imgur.com/3qqYMUc.png" alt="image" style="width:200px;height:200px;">

### Fórmula de Newton - Cotes
Las fórmulas de Newton-Cotes son los tipos de integración numérica más comunes. Se basan en la estrategia de reemplazar una función complicada o datos tabulados por un polinomio de interpolación que es fácil de integrar.

### Regla del trapecio
Esta regla se deduce a partir de la resolución de la integral aplicada sobre el polinomio de grado uno de Lagrange

![equation](https://latex.codecogs.com/svg.image?\int_{a}^{b}f(x)d(x)=\frac{h}{2}\cdot(f(x_{0})&plus;f(x_{1}))-\frac{h^{3}}{12}f''(\varepsilon))

#### Desarrollo en Python
```python
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
```

### Regla de Simpson
Esta regla se deduce a partir de la resolución de la integral aplicada sobre el polinomio de segundo grado de Lagrange

![equation](https://latex.codecogs.com/svg.image?\int_{a}^{b}f(x)d(x)=\frac{h}{3}\cdot(f(x_{0})&plus;4\cdot&space;f(x_{1})&plus;f(x_{2}))-\frac{h^{5}}{90}f^{(4)}(\varepsilon))

#### Desarrollo en Python
```python
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
    print("Valor aproximado de la integral:", integral)

def regla_de_Simpson(f, a, b):
    h = (b - a) / 2
    c = (a + b) / 2
    integral = (h / 3) * (f(a) + 4 * f(c) + f(b))
    return integral

if __name__ == '__main__':
    main()
```

### Regla de Simpson 3/8
Esta regla se deduce a partir de la resolución de la integral aplicada sobre el polinomio de tercer grado de Lagrange

![equation](https://latex.codecogs.com/svg.image?\int_{a}^{b}f(x)d(x)=\frac{3h}{8}\cdot(f(x_{0})&plus;3\cdot&space;f(x_{1})&plus;3\cdot&space;f(x_{2})&plus;f(x_{3}))-\frac{3h^5}{80}f^{(6)}(\xi))

#### Desarrollo en Python
```python
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
```

### Regla de Boole
Esta regla se deduce a partir de la resolución de la integral aplicada sobre el polinomio de cuarto grado de Lagrange

![equation](https://latex.codecogs.com/svg.image?\int_{a}^{b}f(x)d(x)=\frac{2h}{45}\cdot(7\cdot&space;f(x_{0})&plus;32\cdot&space;f(x_{1})&plus;12\cdot&space;f(x_{2})&plus;32\cdot&space;f(x_{3})&plus;7\cdot&space;f(x_{4}))-\frac{8h^5}{945}f^{(6)}(\xi))

#### Desarrollo en Python
```python
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
```


## Bibliografía
- Chapra, S. C., & Canale, R. P. (2010). Métodos numéricos para ingenieros (5a ed.). México: McGrawHill.