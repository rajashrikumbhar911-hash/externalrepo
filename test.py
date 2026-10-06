import pytest
from calculator import add, sub, mul, div

def test_add():
    assert add(10,20)== 30
  # asesrt original value == expected value

def test_sub():
    assert sub(20,10)== 10


def test_mul():
    assert mul(10,10)== 100


def test_div():
    assert div(20,2)== 10