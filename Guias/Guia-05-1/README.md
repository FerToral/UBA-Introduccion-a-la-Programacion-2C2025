# Práctica Haskell · Ejercicios tipo parcial

Tres problemas de la práctica publicada el 20/09/2025. Implementaciones en [TipoParcial.hs](src/TipoParcial.hs).

| Bloque | Ejercicios y contratos |
|---|---|
| Stock, 1–4 | Contar productos distintos; consultar stock (0 si no existe); valorar cantidades por precios; descontar 20% **sólo con stock>10**, conservando orden y cantidad de precios. Nombres únicos en stock/precios; cada producto almacenado tiene precio. |
| Sopa de números, 5–8 | Máximo, valor más repetido, valores de un camino y comparación con Fibonacci desde el índice dado. Tablero rectangular, no vacío, de positivos. El camino avanza derecha/abajo y usa coordenadas **desde uno**. Empates de frecuencia: primera aparición. |
| Perfectos/amigos, 9–12 | Divisores propios crecientes; amistad entre números distintos; primeros n perfectos; pares de amigos de una lista de positivos distintos, sin duplicar el par invertido. |

`generarStock` retoma la práctica personal recuperada; adapta sus cantidades a `Int`, como pide la firma de esta guía. Las demás resoluciones completan el bloque.

La suma de divisores para explorar perfectos recorre pares divisor/cociente hasta la raíz cuadrada sin repetir el divisor de un cuadrado. Se comprobaron los cuatro primeros: 6, 28, 496 y 8128. La búsqueda no es adecuada para pedir muchos perfectos; tampoco se reemplaza por una tabla fija.

Las implementaciones usan patrones, guardas, recursión, operadores y auxiliares propios compatibles con la lista de funciones válidas 2C2025. El ejecutor de pruebas sí utiliza biblioteca estándar: no forma parte de las funciones de una entrega.

Fuente: práctica Haskell del campus 674, recurso 67053. Pruebas: `python herramientas/comprobar.py --haskell`.
