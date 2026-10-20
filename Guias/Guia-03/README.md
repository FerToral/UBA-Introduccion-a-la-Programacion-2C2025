# Guía 3 · Introducción a Haskell

Funciones parciales, guardas, patrones, composición, tuplas y renombres de tipos. Código en [Guia03.hs](src/Guia03.hs); comprobaciones en [Haskell.hs](../../pruebas/Haskell.hs).

## Actividades y contratos

| Ejercicio | Desarrollo |
|---|---|
| 1 | Tablas de `f` y `g`, composición `h=f∘g`, `k=g∘f`. Sólo se admiten los tres argumentos de cada tabla. |
| 2a–c | Valor absoluto y máximos: el resultado pertenece a los valores comparados y es mayor o igual a ellos. |
| 2d–e | Ceros en racionales: disyunción/conjunción y variantes equivalentes por patrones. |
| 2f | Misma clase entre (−∞,3], (3,7] y (7,∞); los extremos no se redondean. |
| 2g | Suma del conjunto de los tres enteros, sin multiplicar las apariciones repetidas. |
| 2h–j | Divisibilidad con divisor positivo; unidades del valor absoluto; decenas de un entero mayor que 9. |
| 3 | Con ambos enteros distintos de cero, existe un entero k no nulo que satisface a²+abk=0 exactamente cuando b divide a. |
| 4a–c, i | Producto interno, comparación estricta coordenada a coordenada y distancia euclídea. `Punto2D` abrevia el par de reales de los incisos iniciales. |
| 4d–f | Suma de terna, suma de múltiplos con divisor positivo, primera posición par desde 1 o 4 si no existe. |
| 4g–h | Construcción e inversión de pares polimórficos. |
| 5 | `fTramos` y `gParidad`: nombres independientes de las tablas del ejercicio 1. Se sigue la desigualdad **f(x)>g(x)** del contrato, aunque el título diga “menores”. |
| 6 | Año bisiesto: divisible por 400, o divisible por 4 y no por 100. |
| 7 | Distancia Manhattan en tres dimensiones; `Punto3D` conserva el mismo tipo del inciso a. |
| 8 | Compara la suma de las últimas dos cifras absolutas: devuelve 1 si la primera suma es menor, −1 si es mayor y 0 si empatan. |

Las operaciones sobre `Float` representan reales con precisión finita; las pruebas usan tolerancia, no igualdad decimal exacta.

## Ejercicio 9 · Leer y especificar programas

- **f1:** dominio real; vale 1 en cero y 0 fuera de cero.
- **f2:** función parcial, dominio {−1,1}; devuelve 15n. Fuera de ese dominio no hay guarda aplicable.
- **f3:** vale 7 para n≤9 y 5 para n>9. Entre 3 y 9 se satisface también la segunda guarda, pero tiene prioridad la primera.
- **f4:** recibe dos reales y devuelve su media aritmética.
- **f5:** la misma media, con un único argumento de tipo par.
- **f6:** compara el entero obtenido al truncar el primer argumento hacia cero con el segundo. No equivale al piso para reales negativos.

## Material y ejecución

Fuente: guía 3 del campus 674, PDF compilado el 05/09/2025. Relación teórica: funciones, evaluación, tipos y patrones. La descripción de arriba permite trabajar sin abrir el PDF; el original docente se conserva en el respaldo de la cursada.

Desde la raíz: `ghci -iGuias/Guia-03/src Guias/Guia-03/src/Guia03.hs`.
Pruebas del bloque funcional: `python herramientas/comprobar.py --haskell`.
