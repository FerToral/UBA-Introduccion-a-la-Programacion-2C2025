module Guia05 where

-- 1 y 2: listas polimórficas.
longitud :: [a] -> Integer
longitud [] = 0
longitud (_:xs) = 1 + longitud xs
ultimo :: [a] -> a
ultimo [x] = x
ultimo (_:xs) = ultimo xs
principio :: [a] -> [a]
principio [_] = []
principio (x:xs) = x:principio xs
reverso :: [a] -> [a]
reverso [] = []
reverso (x:xs) = reverso xs ++ [x]
pertenece :: Eq a => a -> [a] -> Bool
pertenece _ [] = False
pertenece e (x:xs) = e == x || pertenece e xs
todosIguales :: Eq a => [a] -> Bool
todosIguales [] = True
todosIguales [_] = True
todosIguales (x:y:xs) = x == y && todosIguales (y:xs)
todosDistintos :: Eq a => [a] -> Bool
todosDistintos [] = True
todosDistintos (x:xs) = not (pertenece x xs) && todosDistintos xs
hayRepetidos :: Eq a => [a] -> Bool
hayRepetidos xs = not (todosDistintos xs)
quitar :: Eq a => a -> [a] -> [a]
quitar _ [] = []
quitar e (x:xs) | e == x = xs
                | otherwise = x:quitar e xs
quitarTodos :: Eq a => a -> [a] -> [a]
quitarTodos _ [] = []
quitarTodos e (x:xs) | e == x = quitarTodos e xs
                     | otherwise = x:quitarTodos e xs
eliminarRepetidos :: Eq a => [a] -> [a]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs) = x:eliminarRepetidos (quitarTodos x xs)
mismosElementos :: Eq a => [a] -> [a] -> Bool
mismosElementos xs ys = incluidos xs ys && incluidos ys xs
  where incluidos [] _ = True
        incluidos (a:as) bs = pertenece a bs && incluidos as bs
capicua :: Eq a => [a] -> Bool
capicua xs = xs == reverso xs

-- 3. Operaciones numéricas.
sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs
productoria :: [Integer] -> Integer
productoria [] = 1
productoria (x:xs) = x * productoria xs
maximo :: [Integer] -> Integer
maximo [x] = x
maximo (x:xs) | x >= resto = x
               | otherwise = resto
  where resto = maximo xs
sumarN :: Integer -> [Integer] -> [Integer]
sumarN _ [] = []
sumarN n (x:xs) = (n+x):sumarN n xs
sumarElPrimero, sumarElUltimo :: [Integer] -> [Integer]
sumarElPrimero xs@(x:_) = sumarN x xs
sumarElUltimo xs = sumarN (ultimo xs) xs
pares :: [Integer] -> [Integer]
pares xs = multiplosDeN 2 xs
multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN _ [] = []
multiplosDeN n (x:xs) | mod x n == 0 = x:multiplosDeN n xs
                     | otherwise = multiplosDeN n xs
ordenar :: [Integer] -> [Integer]
ordenar [] = []
ordenar xs = ordenar (quitar mayor xs) ++ [mayor]
  where mayor = maximo xs

-- 4. Un blanco es el carácter espacio, no cualquier carácter de control.
type Texto = [Char]
sacarBlancosRepetidos :: Texto -> Texto
sacarBlancosRepetidos (' ':' ':xs) = sacarBlancosRepetidos (' ':xs)
sacarBlancosRepetidos (x:xs) = x:sacarBlancosRepetidos xs
sacarBlancosRepetidos [] = []
palabras :: Texto -> [Texto]
palabras [] = []
palabras (' ':xs) = palabras xs
palabras xs = primera xs : palabras (resto xs)
  where primera [] = []
        primera (' ':_) = []
        primera (a:as) = a:primera as
        resto [] = []
        resto (' ':as) = as
        resto (_:as) = resto as
contarPalabras :: Texto -> Integer
contarPalabras xs = longitud (palabras xs)
palabraMasLarga :: Texto -> Texto
palabraMasLarga xs = elegir (palabras xs)
  where elegir [a] = a
        elegir (a:as) | longitud a >= longitud siguiente = a
                       | otherwise = siguiente
          where siguiente = elegir as
aplanar :: [Texto] -> Texto
aplanar [] = []
aplanar (x:xs) = x ++ aplanar xs
aplanarConBlancos :: [Texto] -> Texto
aplanarConBlancos xs = aplanarConNBlancos xs 1
aplanarConNBlancos :: [Texto] -> Integer -> Texto
aplanarConNBlancos [] _ = []
aplanarConNBlancos [x] _ = x
aplanarConNBlancos (x:xs) n = x ++ blancos n ++ aplanarConNBlancos xs n
  where blancos 0 = []
        blancos j = ' ':blancos (j-1)

-- 5. Acumulados y descomposición con multiplicidad.
sumaAcumulada :: Num a => [a] -> [a]
sumaAcumulada xs = acumular 0 xs
  where acumular _ [] = []
        acumular acc (x:resto) = (acc+x):acumular (acc+x) resto
descomponerEnPrimos :: [Integer] -> [[Integer]]
descomponerEnPrimos [] = []
descomponerEnPrimos (x:xs) = factores x 2 : descomponerEnPrimos xs
  where factores 1 _ = []
        factores n d | mod n d == 0 = d:factores (div n d) d
                     | otherwise = factores n (d+1)

-- 6. Agenda con nombres únicos.
type Nombre = Texto
type Telefono = Texto
type Contacto = (Nombre,Telefono)
type ContactosTel = [Contacto]
elNombre :: Contacto -> Nombre
elNombre (n,_) = n
elTelefono :: Contacto -> Telefono
elTelefono (_,t) = t
enLosContactos :: Nombre -> ContactosTel -> Bool
enLosContactos _ [] = False
enLosContactos n ((nombre,_):xs) = n == nombre || enLosContactos n xs
agregarContacto :: Contacto -> ContactosTel -> ContactosTel
agregarContacto nuevo [] = [nuevo]
agregarContacto nuevo (x:xs) | elNombre nuevo == elNombre x = nuevo:xs
                            | otherwise = x:agregarContacto nuevo xs
eliminarContacto :: Nombre -> ContactosTel -> ContactosTel
eliminarContacto _ [] = []
eliminarContacto n (x:xs) | n == elNombre x = xs
                         | otherwise = x:eliminarContacto n xs

-- 7. True significa libre, no ocupado.
type Identificacion = Integer
type Ubicacion = Texto
type Disponibilidad = Bool
type Estado = (Disponibilidad,Ubicacion)
type Locker = (Identificacion,Estado)
type MapaDeLockers = [Locker]
existeElLocker :: Identificacion -> MapaDeLockers -> Bool
existeElLocker _ [] = False
existeElLocker i ((j,_):xs) = i == j || existeElLocker i xs
ubicacionDelLocker :: Identificacion -> MapaDeLockers -> Ubicacion
ubicacionDelLocker i ((j,(_,u)):xs) | i == j = u
                                  | otherwise = ubicacionDelLocker i xs
estaDisponibleElLocker :: Identificacion -> MapaDeLockers -> Bool
estaDisponibleElLocker i ((j,(libre,_)):xs) | i == j = libre
                                          | otherwise = estaDisponibleElLocker i xs
ocuparLocker :: Identificacion -> MapaDeLockers -> MapaDeLockers
ocuparLocker i ((j,(_,u)):xs) | i == j = (j,(False,u)):xs
ocuparLocker i (x:xs) = x:ocuparLocker i xs
