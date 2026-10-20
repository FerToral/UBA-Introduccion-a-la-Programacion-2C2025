module Guia04 where

-- Precondiciones por ejercicio en README. Recursión explícita.
fibonacci :: Integer -> Integer
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci (n-1) + fibonacci (n-2)
parteEntera :: Float -> Integer
parteEntera x | x < 1 = 0
             | otherwise = 1 + parteEntera (x-1)
esDivisible :: Integer -> Integer -> Bool
esDivisible n d | n == 0 = True
                | n < d = False
                | otherwise = esDivisible (n-d) d
sumaImpares :: Integer -> Integer
sumaImpares 0 = 0
sumaImpares n = 2*n-1 + sumaImpares (n-1)
medioFact :: Integer -> Integer
medioFact 0 = 1
medioFact 1 = 1
medioFact n = n * medioFact (n-2)
todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n | n < 10 = True
                      | otherwise = mod n 10 == mod (div n 10) 10 && todosDigitosIguales (div n 10)
cantDigitos :: Integer -> Integer
cantDigitos n | n < 10 = 1
              | otherwise = 1 + cantDigitos (div n 10)
iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n i = mod (div n (10^(cantDigitos n-i))) 10
sumaDigitos :: Integer -> Integer
sumaDigitos n | n < 10 = n
              | otherwise = mod n 10 + sumaDigitos (div n 10)
esCapicua :: Integer -> Bool
esCapicua n = n == invertirNumero n 0
  where invertirNumero 0 acc = acc
        invertirNumero x acc = invertirNumero (div x 10) (10*acc + mod x 10)
f1 :: Integer -> Integer
f1 0 = 1
f1 n = 2^n + f1 (n-1)
f2, f3, f4 :: Integer -> Float -> Float
f2 0 _ = 0
f2 n q = q^n + f2 (n-1) q
f3 n q = f2 (2*n) q
f4 n q = sumaDesde n (2*n)
  where sumaDesde a b | a > b = 0
                      | otherwise = q^a + sumaDesde (a+1) b
factorial :: Integer -> Integer
factorial 0 = 1
factorial n = n * factorial (n-1)
eAprox :: Integer -> Float
eAprox 0 = 1
eAprox n = 1 / fromIntegral (factorial n) + eAprox (n-1)
-- Diez términos: índices 0 a 9.
e :: Float
e = eAprox 9
raizDe2Aprox :: Integer -> Float
raizDe2Aprox n = sucesion n - 1
  where sucesion 1 = 2
        sucesion j = 2 + 1 / sucesion (j-1)
-- Ejercicio 13: sumatoria doble de i^j (no i*j).
f :: Integer -> Integer -> Integer
f 0 _ = 0
f n m = potencias n m + f (n-1) m
  where potencias _ 0 = 0
        potencias i j = i^j + potencias i (j-1)
sumaPotencias :: Integer -> Integer -> Integer -> Integer
sumaPotencias _ 0 _ = 0
sumaPotencias q n m = fila m + sumaPotencias q (n-1) m
  where fila 0 = 0
        fila b = q^(n+b) + fila (b-1)
sumaRacionales :: Integer -> Integer -> Float
sumaRacionales 0 _ = 0
sumaRacionales n m = fila m + sumaRacionales (n-1) m
  where fila 0 = 0
        fila q = fromIntegral n / fromIntegral q + fila (q-1)
menorDivisor :: Integer -> Integer
menorDivisor n = buscar 2
  where buscar d | mod n d == 0 = d
                 | otherwise = buscar (d+1)
esPrimo :: Integer -> Bool
esPrimo n = n > 1 && menorDivisor n == n
mcd :: Integer -> Integer -> Integer
mcd a 0 = a
mcd a b = mcd b (mod a b)
sonCoprimos :: Integer -> Integer -> Bool
sonCoprimos a b = mcd a b == 1
nEsimoPrimo :: Integer -> Integer
nEsimoPrimo n = buscar 2 n
  where buscar x pendientes | esPrimo x && pendientes == 1 = x
                             | esPrimo x = buscar (x+1) (pendientes-1)
                             | otherwise = buscar (x+1) pendientes
esFibonacci :: Integer -> Bool
esFibonacci n = buscar 0 1
  where buscar a b | a == n = True
                   | a > n = False
                   | otherwise = buscar b (a+b)
mayorDigitoPar :: Integer -> Integer
mayorDigitoPar n | n < 10 = valor (mod n 10)
                 | otherwise = mayor (valor (mod n 10)) (mayorDigitoPar (div n 10))
  where valor d | mod d 2 == 0 = d
                | otherwise = -1
        mayor a b | a > b = a
                  | otherwise = b
esSumaInicialDePrimos :: Integer -> Bool
esSumaInicialDePrimos n = buscar 0 2
  where buscar acc candidato | acc == n = True
                             | acc > n = False
                             | esPrimo candidato = buscar (acc+candidato) (candidato+1)
                             | otherwise = buscar acc (candidato+1)
sumaDivisores :: Integer -> Integer
sumaDivisores n = sumar 1
  where sumar d | d > n = 0
                 | mod n d == 0 = d + sumar (d+1)
                 | otherwise = sumar (d+1)
tomaValorMax :: Integer -> Integer -> Integer
tomaValorMax a b | a == b = a
                 | sumaDivisores a >= sumaDivisores resto = a
                 | otherwise = resto
  where resto = tomaValorMax (a+1) b
pitagoras :: Integer -> Integer -> Integer -> Integer
pitagoras m n r = filas m
  where filas p | p < 0 = 0
                 | otherwise = columnas p n + filas (p-1)
        columnas p q | q < 0 = 0
                     | p*p+q*q <= r*r = 1 + columnas p (q-1)
                     | otherwise = columnas p (q-1)
