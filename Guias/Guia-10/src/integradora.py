"""Práctica integradora: veterinaria, escape, juegos, colas y hospital."""

from queue import Queue as Cola


def stock_productos(stock_cambios: list[tuple[str, int]]) -> dict[str, tuple[int, int]]:
    extremos = {}
    for producto, cantidad in stock_cambios:
        if producto not in extremos:
            extremos[producto] = cantidad, cantidad
        menor, mayor = extremos[producto]
        if cantidad < menor:
            menor = cantidad
        if cantidad > mayor:
            mayor = cantidad
        extremos[producto] = menor, mayor
    return extremos


def es_primo(n: int) -> bool:
    if n < 2:
        return False
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True


def filtrar_codigos_primos(codigos_barra: list[int]) -> list[int]:
    res = []
    for codigo in codigos_barra:
        if es_primo(abs(codigo) % 1000):
            res.append(codigo)
    return res


def subsecuencia_mas_larga(tipos_pacientes_atendidos: list[str]) -> int:
    inicio = mejor_inicio = longitud = mejor_longitud = 0
    for i, animal in enumerate(tipos_pacientes_atendidos):
        if animal == "perro" or animal == "gato":
            if longitud == 0:
                inicio = i
            longitud += 1
            if longitud > mejor_longitud:
                mejor_inicio, mejor_longitud = inicio, longitud
        else:
            longitud = 0
    return mejor_inicio


def un_responsable_por_turno(
    grilla_horaria: list[list[str]],
) -> list[tuple[bool, bool]]:
    res = []
    for dia in range(len(grilla_horaria[0])):
        manana = tarde = True
        for hora in range(1, 4):
            manana = manana and grilla_horaria[hora][dia] == grilla_horaria[0][dia]
            tarde = tarde and grilla_horaria[hora + 4][dia] == grilla_horaria[4][dia]
        res.append((manana, tarde))
    return res


def salidas_validas(tiempos: list[int]) -> tuple[int, float]:
    cantidad = 0
    total = 0
    for tiempo in tiempos:
        if 0 < tiempo < 61:
            cantidad += 1
            total += tiempo
    promedio = 0.0
    if cantidad > 0:
        promedio = total / cantidad
    return cantidad, promedio


def promedio_de_salidas(registro: dict[str, list[int]]) -> dict[str, tuple[int, float]]:
    res = {}
    for integrante, salidas in registro.items():
        res[integrante] = salidas_validas(salidas)
    return res


def tiempo_mas_rapido(tiempos_salas: list[int]) -> int:
    mejor = -1
    for i, tiempo in enumerate(tiempos_salas):
        if 1 <= tiempo <= 60 and (mejor == -1 or tiempo < tiempos_salas[mejor]):
            mejor = i
    return mejor


def racha_mas_larga(tiempos: list[int]) -> tuple[int, int]:
    inicio = mejor_inicio = longitud = mejor_longitud = 0
    for i, tiempo in enumerate(tiempos):
        if 1 <= tiempo <= 60:
            if longitud == 0:
                inicio = i
            longitud += 1
            if longitud > mejor_longitud:
                mejor_inicio, mejor_longitud = inicio, longitud
        else:
            longitud = 0
    return mejor_inicio, mejor_inicio + mejor_longitud - 1


def escape_en_solitario(amigos_por_salas: list[list[int]]) -> list[int]:
    res = []
    for i, sala in enumerate(amigos_por_salas):
        if sala[0] == 0 and sala[1] == 0 and sala[2] != 0 and sala[3] == 0:
            res.append(i)
    return res


def torneo_de_gallinas(estrategias: dict[str, str]) -> dict[str, int]:
    res = {}
    desvios = 0
    for estrategia in estrategias.values():
        if estrategia == "me desvío siempre":
            desvios += 1
    firmes = len(estrategias) - desvios
    for jugador, estrategia in estrategias.items():
        if estrategia == "me desvío siempre":
            res[jugador] = -10 * (desvios - 1) - 15 * firmes
        else:
            res[jugador] = 10 * desvios - 5 * (firmes - 1)
    return res


def reordenar_cola_priorizando_vips(filaClientes: Cola[tuple[str, str]]) -> Cola[str]:
    respaldo = Cola()
    comunes = Cola()
    vips = Cola()
    while not filaClientes.empty():
        afiliado = filaClientes.get()
        respaldo.put(afiliado)
        if afiliado[1] == "vip":
            vips.put(afiliado[0])
        else:
            comunes.put(afiliado[0])
    while not comunes.empty():
        vips.put(comunes.get())
    while not respaldo.empty():
        filaClientes.put(respaldo.get())
    return vips


def cuantos_sufijos_son_palindromos(texto: str) -> int:
    cantidad = 0
    for inicio in range(len(texto)):
        izquierda, derecha = inicio, len(texto) - 1
        palindromo = True
        while izquierda < derecha:
            if texto[izquierda] != texto[derecha]:
                palindromo = False
                break
            izquierda += 1
            derecha -= 1
        if palindromo:
            cantidad += 1
    return cantidad


def quien_gano_el_tateti_facilito(tablero: list[list[str]]) -> int:
    gana_x = gana_o = False
    for fila in range(len(tablero) - 2):
        for columna in range(len(tablero)):
            ficha = tablero[fila][columna]
            if ficha == tablero[fila + 1][columna] == tablero[fila + 2][columna]:
                gana_x = gana_x or ficha == "X"
                gana_o = gana_o or ficha == "O"
    if gana_x and gana_o:
        return 3
    if gana_x:
        return 1
    if gana_o:
        return 2
    return 0


def orden_de_atencion(urgentes: Cola[int], postergables: Cola[int]) -> Cola[int]:
    res = Cola()
    # Al rotar exactamente el tamaño inicial, ambas entradas quedan iguales.
    for _ in range(urgentes.qsize()):
        urgente = urgentes.get()
        postergable = postergables.get()
        urgentes.put(urgente)
        postergables.put(postergable)
        res.put(urgente)
        res.put(postergable)
    return res


def alarma_epidemiologica(
    registros: list[tuple[int, str]], infecciosas: list[str], umbral: float
) -> dict[str, float]:
    cantidades = {}
    for _, enfermedad in registros:
        if enfermedad in infecciosas:
            cantidades[enfermedad] = cantidades.get(enfermedad, 0) + 1
    res = {}
    for enfermedad, cantidad in cantidades.items():
        proporcion = cantidad / len(registros)
        if proporcion >= umbral:
            res[enfermedad] = proporcion
    return res


def empleados_del_mes(horas: dict[int, list[int]]) -> list[int]:
    res = []
    maximo = None
    for empleado, jornadas in horas.items():
        total = 0
        for cantidad in jornadas:
            total += cantidad
        if maximo is None or total > maximo:
            maximo = total
            res = [empleado]
        elif total == maximo:
            res.append(empleado)
    return res


def nivel_de_ocupacion(camas_por_piso: list[list[bool]]) -> list[float]:
    res = []
    cantidad = 0
    camas = len(camas_por_piso[0])
    for piso in range(len(camas_por_piso)):
        for cama in range(camas):
            if camas_por_piso[piso][cama]:
                cantidad += 1
        res.append(cantidad / camas)
        cantidad = 0
    return res
