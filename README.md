# Métodos numéricos
Los métodos numéricos son aquellas técnicas y algoritmos para resolver problemas matemáticos de manera aproximada utilizando cálculos numéricos y computacionales. Estos métodos son especialmente útiles cuando no es posible obtener una solución exacta o analítica utilizando métodos algebraicos o cuando los cálculos analíticos son demasiado complejos o costosos computacionalmente.

## Cifras significativas

### ¿Qué son?
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
- Error absoluto: (completar)$$ p - p $$
- Error relativo: (completar)
- Error porcentual: (completar)

## Análisis de errores en métodos iterativos
En los métodos iterativos siempre vamos a hacer el supuesto de que el valor obtenido en la siguiente ejecución será una mejor aproximación al valor real.
- Error absoluto: (completar)
- Error relativo: (completar)

### Criterio de parada
Una de las preguntas que surge cuando se emplean métodos iterativos, es: **¿Cuándo es suficiente una aproximación?** En ese sentido, siempre dependerá del contexto del problema. Sin embargo, nosotros definiremos un criterio conservador para obtener tantas cifras significativas.
En este caso diremos que **p** es una mejor aproximación a **p** con **d** cifras significativas, si **d** es el mayor número natural que verifique (completar)

## Métodos cerrados

Son aquellos métodos que aprovechan el hecho de que una función cambia de signo en la vecindad de una raíz. A estas técnicas se les llama métodos cerrados, o de intervalos, porque se necesita de dos valores iniciales para la raíz. Como su nombre lo indica, dichos valores iniciales deben “encerrar”, o estar a ambos lados de la raíz.
(Adjuntar imagen de ejemplo)

### Método de bisección
El método de bisección es un método numérico utilizado para encontrar la raíz de una función en un intervalo dado. El método se basa en el teorema de Bolzano, que establece que si una función es continua en un intervalo y los valores de la función en los extremos del intervalo tienen signos opuestos, entonces existe al menos una raíz en ese intervalo.
(insertar imagen de ejemplo)

## Métodos abiertos
Son aquellos métodos que  se basan en fórmulas que requieren únicamente de un solo valor de inicio x o que empiecen con un par de ellos, pero que no necesariamente encierran la raíz. Éstos, algunas veces divergen o se alejan de la raíz verdadera a medida que se avanza en el cálculo. Sin embargo, cuando los métodos abiertos convergen, en general lo hacen mucho más rápido que los métodos cerrados. (Adjuntar imagen de ejemplo)

## Bibliografía
- Chapra, S. C., & Canale, R. P. (2010). Métodos numéricos para ingenieros (5a ed.). México: McGrawHill.
