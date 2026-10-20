module Guia03 where

-- 1. Funciones parciales: los dominios son {1,4,16} y {8,16,131}.
f, g, h, k :: Integer -> Integer
f 1 = 8
f 4 = 131
f 16 = 16
g 8 = 16
g 16 = 4
g 131 = 1
h n = f (g n)
k n = g (f n)

-- 2. Funciones básicas y clases de equivalencia.
absoluto :: Integer -> Integer
absoluto n | n < 0 = -n
           | otherwise = n
mayor :: Ord a => a -> a -> a
mayor a b | a > b = a
          | otherwise = b
maximoAbsoluto :: Integer -> Integer -> Integer
maximoAbsoluto a b = mayor (absoluto a) (absoluto b)
maximo3 :: Integer -> Integer -> Integer -> Integer
maximo3 a b c = mayor a (mayor b c)
algunoEsCero, ambosSonCero, algunoEsCeroPM, ambosSonCeroPM :: Rational -> Rational -> Bool
algunoEsCero a b = a == 0 || b == 0
ambosSonCero a b = a == 0 && b == 0
algunoEsCeroPM 0 _ = True
algunoEsCeroPM _ 0 = True
algunoEsCeroPM _ _ = False
ambosSonCeroPM 0 0 = True
ambosSonCeroPM _ _ = False
enMismoIntervalo :: Float -> Float -> Bool
enMismoIntervalo a b = intervalo a == intervalo b
  where intervalo x | x <= 3 = (0 :: Integer)
                    | x <= 7 = 1
                    | otherwise = 2
sumaDistintos :: Integer -> Integer -> Integer -> Integer
sumaDistintos a b c | a == b && b == c = a
                    | a == b = a + c
                    | a == c = a + b
                    | b == c = a + b
                    | otherwise = a + b + c
-- El segundo argumento es positivo.
esMultiploDe :: Integer -> Integer -> Bool
esMultiploDe n d = mod n d == 0
digitoUnidades, digitoDecenas :: Integer -> Integer
digitoUnidades n = mod (absoluto n) 10
digitoDecenas n = mod (div (absoluto n) 10) 10

-- 3. Con a,b no nulos: a²+abk=0 equivale a a=-bk.
estanRelacionados :: Integer -> Integer -> Bool
estanRelacionados a b = mod a b == 0

-- 4. La firma usa el renombre pedido en el inciso i.
type Punto2D = (Float, Float)
productoInterno :: Punto2D -> Punto2D -> Float
productoInterno (a,b) (c,d) = a*c + b*d
esParMenor :: Punto2D -> Punto2D -> Bool
esParMenor (a,b) (c,d) = a < c && b < d
distancia :: Punto2D -> Punto2D -> Float
distancia (a,b) (c,d) = sqrt ((a-c)^2 + (b-d)^2)
sumaTerna :: (Integer,Integer,Integer) -> Integer
sumaTerna (a,b,c) = a+b+c
sumarSoloMultiplos :: (Integer,Integer,Integer) -> Integer -> Integer
sumarSoloMultiplos (a,b,c) n = sumar a + sumar b + sumar c
  where sumar x | mod x n == 0 = x
                | otherwise = 0
posPrimerPar :: (Integer,Integer,Integer) -> Integer
posPrimerPar (a,b,c) | mod a 2 == 0 = 1
                    | mod b 2 == 0 = 2
                    | mod c 2 == 0 = 3
                    | otherwise = 4
crearPar :: a -> b -> (a,b)
crearPar a b = (a,b)
invertir :: (a,b) -> (b,a)
invertir (a,b) = (b,a)

-- 5. Nombres distintos para no colisionar con f/g del ejercicio 1.
fTramos, gParidad :: Integer -> Integer
fTramos n | n <= 7 = n*n
          | otherwise = 2*n-1
gParidad n | mod n 2 == 0 = div n 2
           | otherwise = 3*n+1
todosMenores :: (Integer,Integer,Integer) -> Bool
todosMenores (a,b,c) = cumple a && cumple b && cumple c
  where cumple x = fTramos x > gParidad x

-- 6 y 7.
type Anio = Integer
type EsBisiesto = Bool
bisiesto :: Anio -> EsBisiesto
bisiesto a = mod a 400 == 0 || (mod a 4 == 0 && mod a 100 /= 0)
type Punto3D = (Float,Float,Float)
distanciaManhattan :: Punto3D -> Punto3D -> Float
distanciaManhattan (a,b,c) (d,e,j) = absolutoReal (a-d) + absolutoReal (b-e) + absolutoReal (c-j)
  where absolutoReal x | x < 0 = -x
                       | otherwise = x

-- 8. El signo del resultado es el especificado, no el de compare.
sumaUltimosDosDigitos :: Integer -> Integer
sumaUltimosDosDigitos x = digitoUnidades x + digitoDecenas x
comparar :: Integer -> Integer -> Integer
comparar a b | sa < sb = 1
             | sa > sb = -1
             | otherwise = 0
  where sa = sumaUltimosDosDigitos a
        sb = sumaUltimosDosDigitos b
