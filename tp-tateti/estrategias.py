"""
Módulo de estrategias para el juego del Tateti

Este módulo contiene las estrategias para elegir la acción a realizar.
Los alumnos deben implementar la estrategia minimax.

Por defecto, se incluye una estrategia aleatoria como ejemplo base.
"""

import random
from typing import List, Tuple
from tateti import Tateti, JUGADOR_MAX, JUGADOR_MIN

def estrategia_aleatoria(tateti: Tateti, estado: List[List[str]]) -> Tuple[int, int]:
    """
    Estrategia aleatoria: elige una acción al azar entre las disponibles.
  
    Args:
        tateti: Instancia de la clase Tateti
        estado: Estado actual del tablero
        
    Returns:
        Tuple[int, int]: Acción elegida (fila, columna)

    Raises:
        ValueError: Si no hay acciones disponibles
    """
    acciones_disponibles = tateti.acciones(estado)
    if not acciones_disponibles:
        raise ValueError("No hay acciones disponibles")
    
    return random.choice(acciones_disponibles)

def estrategia_minimax(tateti: Tateti, estado: List[List[str]]) -> Tuple[int, int]:
    """
    Estrategia minimax: elige la mejor acción usando el algoritmo minimax.
    
    Args:
        tateti: Instancia de la clase Tateti
        estado: Estado actual del tablero
        
    Returns:
        Tuple[int, int]: Acción elegida (fila, columna)
        
    Raises:
        NotImplementedError: Hasta que el alumno implemente el algoritmo
    """
    # TODO: Implementar algoritmo minimax

    # INSTRUCCIONES:
    # 1. Eliminar la línea 'raise NotImplementedError...' de abajo
    # 2. Implementar el algoritmo minimax aquí
    # 3. La función debe retornar una tupla (fila, columna) con la mejor jugada

    if tateti.test_terminal(estado):
        raise ValueError("La partida ya terminó.")

    acciones = tateti.acciones(estado)
    jugador_actual = tateti.jugador(estado)

    mejor_accion = acciones[0]

    if jugador_actual == JUGADOR_MAX:
        mejor_valor = float("-inf")


        for accion in acciones:
            nuevo_estado = tateti.resultado(estado, accion)
            valor = _minimax(tateti, nuevo_estado)

            if valor > mejor_valor:
                mejor_valor = valor
                mejor_accion = accion
    else:
        mejor_valor = float("inf")

        for accion in acciones:
            nuevo_estado = tateti.resultado(estado, accion)
            valor = _minimax(tateti, nuevo_estado)

            if valor < mejor_valor:
                mejor_valor = valor
                mejor_accion = accion

    return mejor_accion

def _minimax(tateti: Tateti, estado: List[List[str]]) -> float:
    """ Evalúa los posibles resultados desde la perspectiva de X."""

    if tateti.test_terminal(estado):
        return tateti.utilidad(estado, JUGADOR_MAX)

    jugador_actual = tateti.jugador(estado)
    acciones = tateti.acciones(estado)

    if jugador_actual == JUGADOR_MAX:
        mejor_valor = float("-inf")

        for accion in acciones:
            nuevo_estado = tateti.resultado(estado, accion)
            valor = _minimax(tateti, nuevo_estado)
            mejor_valor = max(mejor_valor, valor)

        return mejor_valor

    else:
        mejor_valor = float("inf")

        for accion in acciones:
            nuevo_estado = tateti.resultado(estado, accion)
            valor = _minimax(tateti, nuevo_estado)
            mejor_valor = min(mejor_valor, valor)

        return mejor_valor

