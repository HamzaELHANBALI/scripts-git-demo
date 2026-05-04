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
        raise ValueError("division by zero is allowed")
    return left / right

def power(base: float, exponent: float) -> float:
    return base ** exponent 

def square_root(value: float) -> float:
    if value < 0:
        raise ValueError("square root of a negative number is not allowed")
    return value ** 0.5

def logarithm(value: float, base: float = 10) -> float:     
    if value <= 0:
        raise ValueError("logarithm of non-positive numbers is not allowed")
    if base <= 1:
        raise ValueError("logarithm base must be greater than 1")
    import math
    return math.log(value, base)

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return abs(a)

def lcm(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)  

def is_prime(n: int) -> bool:       
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
