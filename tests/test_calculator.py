import pytest

from pyscripts.calculator import add, divide, multiply, subtract


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 4) == 6


def test_multiply():
    assert multiply(6, 7) == 42


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
    
def test_factorial(num):
     
    if num < 1:
        print("Imposible nombre trop petit")
    elif num == 0:
        return 1

    else:
        fact = 1
        while num > 1:
            fact *= num
            num -= 1
        return fact
