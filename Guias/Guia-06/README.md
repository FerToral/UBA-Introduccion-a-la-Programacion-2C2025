# Guía 6 · Introducción al lenguaje imperativo

Funciones, parámetros, lógica, composición, condicionales, repetición y estado.

- [guia6.py](src/guia6.py): prácticas personales, recorridos y variantes.
- [practicas.py](src/practicas.py): actividades que completan la guía.
- [alcance_variables.py](src/alcance_variables.py): ejemplos ejecutables de argumentos y estado global.
- [tests](tests): resultados, salidas de consola, equivalencia while/for y regresiones.

## Actividades

| Ejercicio | Contrato y resolución |
|---|---|
| 1 | Saludo, dos versos propios con salto de línea, raíz de 2 a cuatro decimales, 2! y perímetro de radio 1. |
| 2 | Saludo parametrizado, raíz con argumento no negativo, Fahrenheit→Celsius, repetición del texto, múltiplo con divisor no nulo, paridad por composición y pizzas redondeando hacia arriba (ocho porciones). |
| 3 | Alguno/ambos cero, nombre entre 3 y 8 caracteres y año bisiesto; expresiones booleanas sin if. |
| 4 | Peso por altura no negativa: 300 kg/m hasta tres metros y 200 kg/m adicionales; utilidad entre 400 y 1000 kg inclusive. Composición de peso y utilidad. |
| 5.1–2 | Doble si par; mismo valor si par o siguiente si impar. |
| 5.3 | Múltiplo de 9 tiene prioridad y devuelve triple; si no, múltiplo de 3 devuelve doble; resto sin cambios. 18 devuelve 54. |
| 5.4–6 | Mensaje según longitud; rangos (<5,10…20,>20); regla simplificada de vacaciones del ejercicio. No es una descripción actual de legislación previsional. |
| 6–7 | While y for: 1…10, pares10…40, diez ecos, cuenta regresiva completa, viaje anual y saltos de veinte años hacia −384. |
| 8 | Ejecuciones simbólicas desarrolladas abajo. |
| 9 | Parámetro local y variable global; código rt/ro y contratos abajo. |

### Decisiones en consignas abiertas

Dos if independientes no garantizan exclusión: para múltiplos de 9 se decide sobre el argumento original, no sobre un número ya duplicado. El programa de rangos no imprime nada entre 5 y 9, que no pertenecen a los casos pedidos.

El viaje de veinte años termina en el punto alcanzable más próximo a −384; en empate usa menos saltos. Es una recta de enteros para el ejercicio, no una conversión de calendarios históricos. La cuenta regresiva ahora recorre todos los enteros hasta uno; las dos variantes personales saltaban de dos en dos.

### 8 · Ejecución simbólica

1. x=5,y=7 → x=12,y=7.
2. x=5,y=7 → z=12 → y=24; x queda5.
3. x=5,y=7 → x="hora" → y="horahora": cambia el tipo de ambas variables.
4. x=False → res=True, x permaneceFalse.
5. x=False → x=True.
6. x=True,y=False → res=False → x=False.

### 9 · Estado

Con g global inicialmente0, tres ro(1) producen2,3,4 y dejan g=3. Tres rt(1,0) producen2,2,2 sin modificar g global.

Contrato de rt: enteros x,g de entrada; devuelve x+g+1 y no modifica al llamador.
Contrato de ro: x de entrada y g global inout; g=g_pre+1 y resultado=x+g.

Fuente: guía6, campus674, PDF06/10/2025. Teoría vinculada: introducción imperativa, estado, control y alcance de variables. Pruebas desde la raíz: `python herramientas/comprobar.py --python`.
