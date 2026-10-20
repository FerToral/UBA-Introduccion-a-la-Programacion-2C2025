# Guía 11 · Medidas de análisis de programas

Comparar tiempos, contar operaciones y estudiar mejor/peor caso. [Código](src/complejidad.py), [pruebas](tests/test_complejidad.py).

## 1 · Sumatorias y tiempos

La guía mezcla dos resultados: ciclo/fórmula suman 1…n−1, mientras la recursión suma 1…n. Antes de comparar rendimiento, las tres versiones de este módulo se igualan a **0+1+…+n**. Con n=10 todas devuelven 55.

Los tiempos fluctúan por carga, reloj, caché y tamaño de los enteros. La fórmula usa un número constante de operaciones aritméticas, pero sobre enteros arbitrarios su costo real no es independiente de la cantidad de bits.

El ciclo es Θ(n) en tiempo y O(1) espacio auxiliar; la recursión Θ(n) en tiempo y pila. Se omiten experimentos recursivos mayores que 400 en vez de elevar el límite de recursión y arriesgar la sesión.

## 2 · Máximo sobre lista, pila y cola

Los mismos valores se cargan en las tres estructuras. En todos los casos hay que examinar n elementos, incluso si el mayor está al inicio o al final: no se conoce una cota que autorice cortar.

Los tiempos difieren por sincronización de Queue/LifoQueue, extracción y restauración. Los experimentos incluyen ese costo y lo declaran; no prueban que una estructura sea universalmente más rápida. La pila se restaura invirtiendo el orden de extracción; la cola, manteniéndolo. No hay consumidores concurrentes.

## 3 · Contar operaciones

Modelo: una unidad por comparación, operación aritmética, asignación y retorno; no se cuentan llamadas ni la instrumentación. Se incluye la comparación final del ciclo.

Para n≥0: ciclo **5n+4**, fórmula **5**, recursión **4n+2**. En la fórmula se cuentan n+1, producto, división, asignación conceptual al resultado y retorno. Los valores de `cuentas_sumatorias` describen este modelo, no instrucciones de máquina.

## 4 · Familia de productos

Con el mismo modelo y n≥0:

| Versión del enunciado | Iteraciones / T(n) | Orden |
|---|---|---|
| 0 | Un producto, asignación y retorno: 3 | Θ(1) |
| 1 | n vueltas: 5n+4 | Θ(n) |
| 2 | k=⌈n/2⌉ vueltas: 5k+4 | Θ(n) |
| 3 | Doble ciclo: 6n²+5n+4 | Θ(n²) |
| 4 | Triple ciclo: 7n³+5n²+5n+4 | Θ(n³) |
| 5 | k=0 si n≤1, si no ⌈log₂n⌉: 5k+4 | Θ(log n) |
| 6 | 2^n recorridos de n posiciones; cambian constantes según los bits | Θ(n·2^n) |

Son conteos bajo costo unitario: los productos enormes y las potencias pueden dominar el tiempo real. No se ejecuta un experimento exponencial sin límite para ilustrar una fórmula.

## 5 · Comparación de implementaciones

| Problema | Comparación y resolución |
|---|---|
| Máxima diferencia | Todos los pares: Θ(n²); máximo y mínimo por separado: Θ(n); ambos en una pasada: Θ(n), menor constante. Requiere lista no vacía para las variantes que indexan s[0]. |
| Suma de productos | n² pares con prueba i≠j frente a n(n−1)/2 pares i<j: ambos Θ(n²). Los programas suman **pares sin orden**, pese a la ambigüedad de la especificación; el módulo lo explicita. |
| Posiciones pares | Examinar n índices o recorrer sólo ⌈n/2⌉: ambos Θ(n); la segunda evita decisiones internas. |
| Multiplicar por índice | Sumas repetidas: Σi=n(n−1)/2, Θ(n²); producto directo por posición: Θ(n). Modifica la misma lista. |
| Diagonal principal | Recorrer toda la matriz n×n: Θ(n²); consultar m[i][i]: Θ(n). |
| Identidad | Ambas variantes escriben n² posiciones: Θ(n²); cambia el trabajo de la rama, no el orden. |
| Suma matricial | Para r×c, las tres variantes son Θ(rc). La que guarda sumas de filas necesita O(r) extra y debe inicializar la lista auxiliar: el código del PDF omite esa inicialización. Aquí se acumula directamente. |

Los conteos exactos de variantes con `mayor`/`menor` dependen de si se cuenta el cuerpo de cada llamada y del resultado de sus decisiones; estas comparaciones expresan el número de recorridos y el orden, no una constante universal.

## 6 · Mejor y peor caso

1. **Sumar pares:** recorre siempre n valores; mejor todos impares, peor todos pares. Ambos Θ(n), distinta cantidad de sumas.
2. **Suma hasta umbral:** mejor el primero no cumple, Θ(1); peor cumplen todos, Θ(n). La lista vacía también termina inmediatamente.
3. **Contar mínimos:** siempre dos recorridos Θ(n); cada nuevo mínimo agrega una asignación y cada aparición del mínimo incrementa el conteo.
4. **Colapsar repetidos:** n−1 comparaciones siempre; mejor todo igual, una salida; peor todos los adyacentes diferentes, salida de tamaño n. Bajo modelo unitario Θ(n); concatenar strings inmutables puede agregar costo cuadrático de copias.
5. **Sumar filas negativas:** para r filas y c columnas, todas positivas hacen Θ(r); todas negativas Θ(rc). El signo de la primera celda determina si se recorre la fila completa por la precondición de signos uniformes.

## Experimentos reproducibles

Desde la raíz:

```shell
python Guias/Guia-11/src/complejidad.py build/experimentos
python herramientas/comprobar.py --python
```

Genera dos CSV con tiempos **medidos**, semilla fija y omisiones identificadas. Se usa un conjunto acotado de tamaños, no el millón de ejecuciones casi iguales sugerido por el gráfico del PDF. Los CSV son resultados del equipo, no respuestas numéricas universales.

Gráfico opcional: instalar matplotlib y ejecutar `python Guias/Guia-11/src/graficar.py build/experimentos/sumatorias.csv build/experimentos/sumatorias.svg`. La escala logarítmica permite comparar los métodos; no se extrapolan tiempos omitidos. La muestra comprobada está en [resultados](resultados).

Fuente: guía de medidas de análisis del campus 674, recurso 69818. La descripción local conserva el hilo entre programas, hipótesis de costo y conclusiones.
