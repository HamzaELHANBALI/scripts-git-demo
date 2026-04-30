"""Fonctions de calcul simples."""


def add(left: float, right: float) -> float:
    """
    Additionne deux nombres et retourne le résultat.
    """
    return left + right


def subtract(left: float, right: float) -> float:
    """
    Soustrait le second nombre du premier et retourne le résultat.
    """
    return left - right


def multiply(left: float, right: float) -> float:
    """
    Multiplie deux nombres et retourne le résultat.
    """
    return left * right


def divide(left: float, right: float) -> float:
    """
    Divise le premier nombre par le second et retourne le résultat.
    """
    if right == 0:
        raise ValueError("division by zero is not allowed")
    return left / right
