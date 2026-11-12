
import pytest
from calculator import Calculator

calc = Calculator()

def test_add():
    assert calc.add(5, 3) == 8
    assert calc.add(-2, 2) == 0
    assert calc.add(0, 0) == 0

def test_subtract():
    assert calc.subtract(10, 4) == 6
    assert calc.subtract(3, 7) == -4

def test_multiply():
    assert calc.multiply(4, 5) == 20
    assert calc.multiply(-3, 2) == -6
    assert calc.multiply(0, 10) == 0

def test_divide():
    assert calc.divide(10, 2) == 5
    assert calc.divide(7, 2) == 3.5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        calc.divide(10, 0)
