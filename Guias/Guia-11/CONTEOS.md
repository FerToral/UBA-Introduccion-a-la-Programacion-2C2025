# Conteos exactos y decisiones de costo

Recurso69818 del campus 674, ejercicios4–6. Son conteos del pseudocódigo
del enunciado, no de las implementaciones Python alternativas del módulo
complejidad.py. [Calculadora](src/cuentas.py) y
[comprobaciones](tests/test_cuentas.py).

## Modelo

Una unidad por asignación, operación aritmética, comparación, append y
return explícito. Los accesos a variables/índices, len y la invocación de
funciones no agregan unidades. Sí se cuenta el cuerpo de las auxiliares:
mayor/menor cuestan3; valor_absoluto cuesta3 si x>0 y4 si x≤0, contando
la negación aritmética. Un return implícito cuesta0.

Se cuenta la última comparación de cada while. and evalúa su derecha sólo
si hace falta, sin costo adicional por el conector. Un if no agrega otra
operación además de evaluar su condición. Potencia y concatenación valen
una operación en este modelo: su costo físico no es constante.

Este modelo preciso permite comparar fórmulas; otro modelo cambia constantes,
no necesariamente el orden. El contador ilustrativo de la guía omite la
comparación final y el return: no se mezcla con este modelo.

## Ejercicio4 · Productos

Para n≥0, k=⌈n/2⌉ y l=0 si n≤1, o l=⌈log₂n⌉ en otro caso:

| Versión | T(n)         | Orden    |
| ------- | ------------ | -------- |
| 0       | 3            | Θ(1)     |
| 1       | 5n+4         | Θ(n)     |
| 2       | 5k+4         | Θ(n)     |
| 3       | 6n²+5n+4     | Θ(n²)    |
| 4       | 7n³+5n²+5n+4 | Θ(n³)    |
| 5       | 5l+4         | Θ(log n) |
| 6       | (10n+9)·2ⁿ+5 | Θ(n·2ⁿ)  |

En la versión6, ambas ramas hacen una multiplicación y una asignación:
los bits **no cambian el conteo unitario**. Hay2ⁿ vueltas externas.
Cada test externo calcula2ⁿ y compara; cada test interno del bit contiene
resta, potencia, división, módulo y comparación. Resultado:
2 iniciales+2(2ⁿ+1)+2ⁿ[2+(n+1)+9n+4]+1.
Las potencias y productos de enteros grandes sí cambian el tiempo real.

## Ejercicio5 · Comparar variantes

n es longitud de lista o lado de matriz cuadrada; P=n(n−1)/2,
k=⌈n/2⌉. En máxima diferencia n≥1; en los restantes conteos el
ciclo también está definido para n=0.

| Problema               | Variante1   | Variante2 | Variante3 |
| ---------------------- | ----------- | --------- | --------- |
| Máxima diferencia      | 11n²+5n+4+B | 14n−6     | 11n−5     |
| Suma de productos      | 7n²+2n+5    | 6P+6n+4   | —         |
| Posiciones pares       | 5n+k+4      | 4k+4      | —         |
| Multiplicar por índice | 5P+7n+2     | 5n+2      | —         |
| Diagonal principal     | 4n²+6n+5    | 4n+5      | —         |
| Matriz identidad       | 5n²+5n+3    | 4n²+6n+3  | —         |

B cuenta pares ordenados(i, j) con s[i]≤s[j], porque la rama no positiva
de valor_absoluto agrega una negación. Si E=Σ frecuencia(x)², entonces
B=(n²+E)/2: los pares desiguales se reparten entre > y <, los iguales
entran todos. B está entre n(n+1)/2 y n². No se atribuye una constante
independiente de los datos a esta variante.

Ejemplo de derivación para suma_de_productos_v2:
2 iniciales+(n+1)tests externos+2npara j=i+1+(P+n)tests internos+
5Ppor suma/producto/asignación e incremento+2nincrementos externos+
1return =6P+6n+4.

En la variante1, el if se evalúa n² veces pero acumula sólo n(n−1).
En posiciones pares, append ocurre k veces. En identidad_v2 se ahorran
n²comparaciones a cambio de n escrituras diagonales: mejora la constante
para n>1, ambas siguen siendo cuadráticas.

### Suma matricial rectangular

Para rfilas y ccolumnas:

| Variante                   | T(r, c)   | Espacio auxiliar |
| -------------------------- | --------- | ---------------- |
| 1, lista de sumas por fila | 5rc+13r+8 | O(r)             |
| 2, acumular cada fila      | 5rc+9r+4  | O(1)             |
| 3, doble while             | 5rc+5r+4  | O(1)             |

sumar_elementos_lista cuesta5c+4. La variante1 requiere inicializar
suma_por_fila=[]: sólo anotar su tipo, como hace el PDF, no crea una lista
y da UnboundLocalError. Se cuenta esa corrección como una asignación.
Para matrices cuadradas sustituir r=c=n. Todas tienen Θ(rc) con r, c≥1.

## Ejercicio6 · Dependencia de los datos

| Problema y parámetros                                                       | T exacto   | Mejor caso                | Peor caso                       |
| --------------------------------------------------------------------------- | ---------- | ------------------------- | ------------------------------- |
| Sumar pares; e elementos pares                                              | 5n+2e+4    | Todos impares:5n+4        | Todos pares:7n+4                |
| Prefijo menor al umbral; longitud k                                         | 6k+4+[k<n] | n>0, primero no cumple:5  | Todos cumplen:6n+4              |
| Contar mínimos; a nuevos mínimos estrictos, m apariciones del mínimo global | 8n+3+a+2m  | Primero mínimo único:8n+5 | Todos iguales:10n+3             |
| Colapsar; d cambios entre adyacentes, n≥1                                   | 5n−1+2d    | Todo igual:5n−1           | Todos adyacentes distintos:7n−3 |
| Sumar filas negativas; rfilas, a negativas y N elementos en ellas           | 4r+5N+2a+4 | Todas positivas:4r+4      | Todas negativas, r×c:5rc+6r+4   |

[k<n] vale1 si el prefijo termina por un elemento que no cumple y0 si llega
al final. El vacío cuesta4 en ese problema. No se evalúa s[n].

Para mínimos, a≤n−m; por eso a+2m≤2n, alcanzado por la lista constante.
Una lista estrictamente decreciente cambia más veces el mínimo, pero **no**
es el peor caso total: agrega menos apariciones en el segundo recorrido.

En colapsar hay n−1 restas del índice anterior y comparaciones; una cadena
sin repeticiones adyacentes concatena n−1 veces. Las copias reales pueden
costar Θ(n²), aunque el conteo unitario sea lineal.

En filas negativas, la precondición exige filas no vacías de signo uniforme
y sin ceros: inspeccionar la primera celda basta para decidir si sumar la fila.
