# Guía 9 · Testing de caja blanca

Cobertura de sentencias y decisiones, casos de prueba, mutantes y código inalcanzable. [Programas de estudio](src/caja_blanca.py), [suite](tests/test_caja_blanca.py). Los sufijos `defectuoso` son ejemplos deliberados: las pruebas muestran por qué no satisfacen el contrato.

La numeración L1… del análisis corresponde al pseudocódigo del enunciado, no a las líneas físicas del módulo.

## 1 · Máximo

Flujo: L1→L2; verdadero→L3→L5, falso→L4→L5.

| Caso | L1 | L2 | L3 | L4 | L5 | L2 verdadera | L2 falsa |
|---|---|---|---|---|---|---|---|
| (0,0)→0 | sí | sí | no | sí | sí | no | sí |
| (0,1)→1 | sí | sí | sí | no | sí | sí | no |

Juntos cubren todas las líneas y las dos decisiones.

## 2 · Mínimo

Mismo grafo que máximo. (0,1) y (1,1) recorren las dos ramas y pasan incluso si ambas devuelven x. Por eso la cobertura completa no detecta este defecto. Agregar (2,1)→1 lo revela: la rama falsa devuelve 2. La corrección devuelve y.

## 3–4 · Sumar y restar

Flujo lineal L1→L2→L3→L4. Un caso alcanza todas las líneas. Para suma, (3,−2)→1 comprueba también signos. Para resta, (3,0)→3 **no** distingue sumar/restar; (3,2)→1 sí lo hace. No hay ramas condicionales.

## 5 · Signo

Flujo: inicialización→x<0; verdadero asigna −1 y termina; falso evalúa x>0; verdadero asigna 1, falso conserva 0. Casos −2, 2 y 0 cubren las cuatro salidas de las dos decisiones. Sólo −2 y 2 alcanzan todas las líneas, pero no la salida falsa de x>0.

## 6 · Valor absoluto defectuoso

Inicializa cero, evalúa x<0 y sólo en verdadero asigna −x. El caso −2 cubre todas las líneas pero no la rama falsa. −2 y 0 cubren ambas ramas y aun así pasan con el defecto; agregar 2→2 lo descubre. La corrección devuelve x para no negativos.

## 7 · Valor absoluto correcto

Condición→retorno −x o retorno x. Casos −2 y 0 cubren líneas y ramas; un positivo añade una clase de entrada útil, aunque no otra rama.

## 8 · Multiplicar por diez

Inicializar resultado/contador→comparar contador<10→sumar/incrementar→volver a comparar; salida falsa→retorno. Cualquier entero, por ejemplo 3→30, recorre el cuerpo diez veces y la salida del ciclo una vez. Un único caso cubre ambas decisiones del ciclo; no es posible cero iteraciones porque el contador inicia en cero.

## 9 · Sumar por unidades

y<0 elige sumando −1 y cantidad −y; de lo contrario +1 y cantidad y. Luego un ciclo suma esa unidad hasta alcanzar la cantidad. (4,−2)→2 y (4,2)→6 recorren ambas ramas y las salidas del ciclo; (4,0)→4 agrega cero iteraciones.

## 10 · MCD

Inicialización→y≠0→resto/intercambio→comparar; falso→retorno. (12,8)→4 recorre cuerpo y salida. (9,0)→9 comprueba cero vueltas; (0,0) devuelve 0 en esta implementación. Dominio: enteros no negativos.

## 11 · Triángulo

Cadena de decisiones: lados positivos→desigualdad triangular→tres iguales→dos iguales→escaleno. Suite: (0,2,2)→4, (1,1,2)→4, (2,2,2)→1, (2,2,3)→2, (3,4,5)→3. Cubre todas las salidas de los **if**; esto no afirma cobertura de cada subcondición booleana ni MC/DC.

## 12 · Multiplicar por absoluto

Después de calcular |y| se pregunta si es negativo. La salida verdadera y su retorno −1 son inalcanzables si el auxiliar cumple su contrato. No se falsea el auxiliar para forzar un 100%. Casos (3,−2)→6, (3,0)→0 y (−3,2)→−6 cubren las rutas alcanzables y el ciclo con/sin iteraciones.

## 13 · Vaciar una secuencia

Inicializar índice→¿hay otro elemento?→asignar cero→avanzar→comparar; salida→fin. Una lista no vacía recorre cuerpo y salida; [] comprueba la ruta sin cuerpo. El contrato exige conservar longitud y modificar la entrada, no crear otra lista.

## 14 · Existe elemento

Inicialización/iteración→comparar elemento; verdadero retorna/interrumpe, falso avanza; agotamiento→falso. Suite: [] y elemento 1→False; [1,2] y 3→False; [1,2] y 1→True; [1,2] y 2→True. Incluye agotamiento, acierto inmediato y acierto tras comparación falsa.

Fuente: guía 9 del campus 674, recurso 69815. Teoría vinculada: grafos de flujo, sentencias, ramas y relación entre cobertura y detección de fallas.

Desde la raíz: `python herramientas/comprobar.py --python`. La suite verifica resultados y contraejemplos; el análisis de cobertura anterior es por rutas del enunciado, no un porcentaje inventado a partir del número de tests.
