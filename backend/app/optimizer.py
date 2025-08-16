from typing import List, Tuple
from app.schemas import Objeto

def optimizar(capacidad: int, objetos: List[Objeto]) -> Tuple[int, List[str], int]:
    """
    Calcula la combinación óptima de proyectos/inversiones usando programación dinámica.

    Parámetros:
    - capacidad (int): Presupuesto máximo disponible
    - objetos (List[Objeto]): Lista de proyectos con peso y ganancia

    Retorna:
    - ganancia_total (int)
    - lista de nombres seleccionados (List[str])
    - peso_total (int)
    """
    pesos = [o.peso for o in objetos]
    ganancias = [o.ganancia for o in objetos]
    n = len(pesos)

    if n == 0:
        return 0, [], 0

    # DP de (n+1) x (capacidad+1)
    dp = [[0] * (capacidad + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        w = pesos[i - 1]
        v = ganancias[i - 1]
        for c in range(capacidad + 1):
            sin_i = dp[i - 1][c]
            con_i = dp[i - 1][c - w] + v if w <= c else -10**18
            dp[i][c] = max(sin_i, con_i)

    # Recuperar selección
    seleccion = []
    c = capacidad
    for i in range(n, 0, -1):
        if dp[i][c] != dp[i - 1][c]:
            seleccion.append(i - 1)
            c -= pesos[i - 1]

    seleccion.reverse()
    ganancia_total = dp[n][capacidad]
    peso_total = sum(pesos[i] for i in seleccion)
    seleccionados = [objetos[i].nombre for i in seleccion]

    return ganancia_total, seleccionados, peso_total
