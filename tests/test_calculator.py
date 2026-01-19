import pytest
from services.calculator_service import add, divide


def test_add():
    assert add(2, 3) == 5


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


# Failing tests
def test_add_fail():
    assert add(2, 2) == 5  


def test_divide_fail():
    assert divide(9, 3) == 2  


def test_divide_by_zero_fail():
    divide(5, 1)
