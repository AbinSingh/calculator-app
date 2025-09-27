import pytest
from app.calculator import Calculator

def test_add():
    assert Calculator().add(2, 3) == 5

def test_subtract():
    assert Calculator().subtract(5, 3) == 2

def test_multiply():
    assert Calculator().multiply(2, 4) == 8

def test_divide():
    assert Calculator().divide(10, 2) == 5
