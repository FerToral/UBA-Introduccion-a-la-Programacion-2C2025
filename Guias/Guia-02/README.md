# Guía 2 · Especificación de problemas

Contratos, secuencias, subespecificación y sustitución. Fuente: campus 674,
recurso 63964 (p2.pdf, 19/08/2025). Resolución posterior y ejemplos propios.
[Contratos ejecutables de apoyo](src/contratos.py) · [pruebas](tests/test_contratos.py).

Notación: |s| es longitud, s[i] el elemento con0≤i<|s|,
apar(x, s) su multiplicidad. Las cláusulas de un contrato se conjugan.
Una precondición verdadera no garantiza que la postcondición sea realizable.

## 1 · Ejemplos y salidas permitidas

| Inciso                     | Entrada  | Salida válida | Observación                                                            |
| -------------------------- | -------- | ------------- | ---------------------------------------------------------------------- |
| a, duplicar                | 3        | 6             | También admite negativos                                               |
| b, raíz                    | 9        | 3             | Requiere positivo; elegir raíz no negativa                             |
| c, entero cercano positivo | 2.2      | 2             | El contrato no es realizable para todo real, aunque requiere True      |
| d, raíces Uno              | ⟨9,4⟩    | ⟨3,2⟩         | Conserva longitud y orden                                              |
| e, Dos                     | ⟨9,4⟩    | ⟨2,3⟩         | Puede permutar                                                         |
| f, Tres                    | ⟨9,4⟩    | ⟨3,3⟩         | Longitud2; sólo exige raíces de uno o varios elementos                 |
| g, Cuatro                  | ⟨−1,9,4⟩ | ⟨3,2⟩         | Raíces de todos los positivos; sin longitud ni orden fijados           |
| h, Cinco                   | ⟨9,4⟩    | ⟨3⟩           | Sólo restringe posiciones existentes comunes; admite prefijos y extras |
| i, Seis                    | ⟨9,4⟩    | ⟨3⟩           | Igual condición posicional, con longitud máxima2                       |

En c, para x=−2 el entero más cercano es−2, que no es positivo:
hay entradas que cumplen el requiere pero no tienen salida.
También falta política explícita de desempate para valores semienteros.
Una reparación posible restringe x>0.5 y admite cualquiera de los enteros
más cercanos; otra pide el entero positivo más cercano, cambiando el problema.

En Cuatro y Dos, la lectura “los elementos son las raíces de todos...”
es de pertenencia/cobertura, no multiplicidad por posición. Se explicitan
a continuación sus consecuencias; no se agregan garantías que el texto omite.

## 2 · Comparar las seis variantes

1. No se puede borrar positividad indiscriminadamente: llamar raíz con un
   valor no positivo incumple su contrato. Cuatro ya filtra positivos;
   en Tres podría guardarse al menos un positivo y elegir sólo de ellos.
   Las variantes con posición fija requieren positivos en cada posición usada.
2. Uno obliga orden; Dos permite permutar. Para⟨9,4⟩,⟨2,3⟩ sirve en Dos
   pero no en Uno;⟨3,2⟩ sirve en ambos. No tienen que dar resultados distintos.
3. Todo algoritmo de Uno satisface Dos. El recíproco es falso.
4. Cinco no fija longitud; Seis sólo fija un máximo, no igualdad.
   Un prefijo de dos raíces para cinco entradas es válido en ambas.
   Para⟨3,9,11⟩, añadir√13 al final vale en Cinco, no en Seis.
5. En Cuatro, agregar longitud|s| puede exigir repetir raíces de positivos
   cuando hay entradas negativas. Para⟨−1,4⟩,⟨2⟩ deja de servir y⟨2,2⟩
   sí cumple la lectura de pertenencia. No vuelve positiva la entrada original.
6. Coincidir en una entrada no prueba equivalencia de contratos.
   Tres admite⟨3,3⟩ para⟨9,4⟩; Dos debe cubrir también la raíz2.
7. Sin “no repetidos”, pertenencia y longitud no conservan multiplicidades:
   para⟨4,1,1⟩,⟨2,2,1⟩ es válida en Dos bajo esa lectura.
   Para garantizar multiplicidades hay que contarlas o fijar posiciones.

## 3 · Ordenar

a: sí. b: no, porque se exige crecimiento estricto y hay dos3.
Si se conserva ese asegura, un requiere posible es “s no tiene repetidos”.
c, d, e: sí según el contrato original:⟨3,4⟩,⟨3,4,5,6⟩ y⟨1,2,3⟩
son crecientes, aunque no son ordenamientos correctos de la entrada.

Para c puede agregarse que todo elemento de s pertenezca a resultado.
Para d, que todo elemento del resultado pertenezca a s. Ninguna sola
condición resuelve todos los defectos. La corrección general, que admite
duplicados, es:

```text
problema ordenar(s: seq<Z>): seq<Z>
requiere: True
asegura: |resultado|=|s|
asegura: para todo i,0<=i<|resultado|-1: resultado[i]<=resultado[i+1]
asegura: para todo x: apar(x, resultado)=apar(x, s)
```

La igualdad de multiplicidades implica longitud; se deja explícita para
facilitar lectura. No se exige un algoritmo particular ni estabilidad
cuando los elementos son sólo enteros.

## 4 · Duplicar todos

a: igual longitud no relaciona valores: para⟨1,2⟩,⟨8,9⟩ cumple el texto
pero no el problema.

b: la tercera cláusula, relación por posición resultado[i]=2s[i],
junto a longitud, es suficiente. La primera garantiza presencia de dobles
pero permite desorden y multiplicidades incorrectas. La segunda es falsa
para0ynegativos. La cuarta(paridad)es necesaria pero no suficiente,
y resulta redundante al fijar cada posición.

## 5 · Frecuencia de colectivos

L={28,33,34,37,45,107,160,166}. Se preserva el orden del registro,
aunque contar no lo necesita.

```text
cantidadColectivosDeLinea(s: seq<Z>, linea:Z):Z
requiere: linea pertenece a L
requiere: todo elemento de s pertenece a L
asegura: resultado=apar(linea, s)

lineaConMejorFrecuencia(a:Z, b:Z, s: seq<Z>):Z
requiere: a, b pertenecen a L
requiere: todo elemento de s pertenece a L
asegura: resultado pertenece a {a, b}
asegura: apar(resultado, s)=max(apar(a, s), apar(b, s))
```

Se interpreta mejor frecuencia como mayor cantidad diaria, no intervalo
promedio: no hay horarios en la entrada. En empate puede elegirse cualquiera;
una implementación determinista elige a. No hace falta exigir a≠b.

## 6 · Calificaciones

Tipos del enunciado: Alumno=String, Materia=String,
Cursada=seq<Materia×R>, CalificacionesDelDC=seq<Alumno×Cursada>.
C es el registro de un alumno. Se asume unicidad de alumnos, notas[0,10]
y que no hay una cursada posterior de una materia ya aprobada.
La posición representa orden temporal; no se agrega unicidad de materias.

a: alumno debe existir y tener|C|>0.
resultado=(Σ nota de cada intento en C)/|C|.
Se promedian **todos los intentos**, no sólo aprobados ni últimas notas:
el texto no pide descartar recursadas.

b: para una materia mejor, requiere|C|>0; resultado es una materia de C
con alguna nota igual al máximo de todas las notas. Empate: cualquiera.
Para todas las mejores, se devuelve cada materia que tenga al menos un
intento con la nota máxima, sin repetidos. No se repite la materia por intento.

c: el resultado contiene exactamente a los alumnos con algún intento
de esa materia de nota≥4, y no repite alumnos. Puede ser vacío.
Para devolverlos ordenados, agregar orden alfabético no decreciente:
fortalece el asegura y **reduce** el conjunto de programas válidos.

d: resultado tiene longitud del registro y, para cada posición i,
contiene el promedio del alumno en esa posición. Requiere que todas las
cursadas sean no vacías; evita una correspondencia ambigua por pertenencia.

Los auxiliares de src/contratos.py hacen operativas estas relaciones con
datos ficticios; no contienen calificaciones personales.

## 7 · Postcondiciones y sustitución

a: un programa de pares1 no necesariamente satisface pares2: puede devolver
⟨4,2⟩ para⟨2,4⟩.
b: todo programa de pares2 satisface pares1.
c: post2 implica post1, pero no al revés; la postcondición de pares2 es más
fuerte. Mismo requiere y mayor garantía permiten sustitución en esa dirección.

## 8 · Precondiciones y sustitución

a: pre3⇒pre2⇒pre1. b: la versión3 tiene dominio más restringido;1, más amplio.
c: la3 permite sumar directamente todos los elementos porque todos superan10
y, por tanto, su valor absoluto supera5. La2sólo filtra>5;1debe admitir signos.
d: para quien llama, la1es más útil: acepta cualquier secuencia entera.
Una implementación de1puede usarse donde se exige2o3, no al revés.
Precondición más fuerte facilita al implementador, pero exige más al usuario.

El nombre sumarAbsMayorA5 no cambia el asegura: se suman los **valores
originales** con |x|>5, no sus valores absolutos. Para⟨−6,7⟩ la salida es1, no13.
