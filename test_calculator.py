from calculator import add, multiply, subtract


def test_add():
    assert add(5, 3) == 8


def test_subtract():
    assert subtract(5, 3) == 1


def test_multiply():
    assert multiply(5, 3) == 15