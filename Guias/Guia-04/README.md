# Guía 4 · Recursión sobre enteros

[Guia04.hs](src/Guia04.hs) trabaja casos base, reducción del argumento e hipótesis recursiva. Cada llamada debe acercarse al caso base; no se usan ciclos ni sumatorias de biblioteca.

| Ejercicios | Funciones y dominio |
|---|---|
| 1–5 | Fibonacci n≥0; parte entera x≥0; divisibilidad n≥0 y divisor>0 **sin div/mod**; suma de los primeros n impares; doble factorial n≥0. |
| 6–9 | Dígitos iguales n>0; i-ésima cifra desde la izquierda con 1≤i≤cantidad; suma de cifras y capicúa para n≥0. Cero tiene una cifra. |
| 10 | f1 suma 2^i desde 0 hasta n; f2 suma q^i desde 1 hasta n; f3 hasta 2n; f4 desde n hasta 2n inclusive. |
| 11 | eAprox n suma 1/i! para i=0…n; e usa **diez términos**, índices 0…9. |
| 12 | Aproximación de raíz de 2 mediante a1=2, an=2+1/a(n−1), resultado an−1; n≥1. |
| 13 | Sumatoria doble de i^j, i=1…n y j=1…m. |
| 14–15 | Sumatoria doble de q^(a+b) y de p/q; los denominadores recorren 1…m. |
| 16 | Menor divisor para n>1, primalidad, coprimalidad y n-ésimo primo con n≥1. |
| 17–19 | Pertenencia a Fibonacci, mayor cifra par (−1 si no existe), suma de un prefijo de primos. Se admite el prefijo vacío para n=0. |
| 20 | Entre a≥1 y b≥a, elige un argumento cuya suma de divisores positivos sea máxima; en empate el menor. |
| 21 | Cuenta pares (p,q) en [0,m]×[0,n] con p²+q²≤r². Los puntos sobre el borde se incluyen. |

## Razonamiento y límites

En `esDivisible` se resta un divisor positivo: termina al llegar a cero o a un resto menor que el divisor. En `pitagoras` se recorren todos los pares del rectángulo, no sólo la circunferencia.

Fibonacci conserva la definición recursiva pedida, de costo exponencial; no es una implementación para índices grandes. Las funciones sobre `Integer` no desbordan enteros de tamaño fijo, pero consumen recursos. `Float` tiene redondeo: `parteEntera` por restas se usa con magnitudes pequeñas; no es un sustituto industrial de `floor`.

Fuente: guía 4 del campus 674, compilada el 15/09/2025. Teoría vinculada: recursión sobre enteros y terminación. Descripciones propias; PDF docente preservado en respaldo.

Pruebas desde la raíz: `python herramientas/comprobar.py --haskell`.
