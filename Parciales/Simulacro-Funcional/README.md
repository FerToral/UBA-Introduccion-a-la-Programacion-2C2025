# Simulacro funcional

Práctica realizada durante la cursada 2C2025 sobre un enunciado identificado como **parcial TM, 1C2025, tema 1**. No es un parcial rendido en otra edición.

[Simulacro.hs](src/Simulacro.hs) conserva las respuestas personales de abundantes, cursadas vencidas y saturación. El conteo de pares se corrige para consultar **una columna**, no todo el prefijo de cada fila, e incluir cero como par.

## Consignas

1. Contar números abundantes en [d,h], con 0<d≤h. Un abundante supera su propio valor con la suma de sus divisores propios.
2. Devolver sin repetidos los nombres de cursadas aprobadas hasta 1C2021 inclusive. Año≥1993; cuatrimestre entre 0 y 2.
3. Recorrer hasta el primer negativo, excluyéndolo; conservar valores entre 0 y u y saturar en u los mayores. u>0.
4. Contar pares de la columna indicada en una matriz rectangular no vacía. La columna empieza en **1**, a diferencia de la guía 5.
5. Patrones incompletos: el programa puede compilar pero falla si se evalúa un argumento no contemplado.
6. La precondición “es vocal o longitud>3” no garantiza texto no vacío: basta que el carácter sea vocal. Una consonante con texto de longitud 2 queda fuera del contrato.

Pruebas conjuntas: `python herramientas/comprobar.py --haskell`. El contraejemplo [[2,3],[4,5]], columna 2, debe dar 0; la respuesta antigua contaba los pares de columnas anteriores.
