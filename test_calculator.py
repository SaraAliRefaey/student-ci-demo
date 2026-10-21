from calculator import add, multiply, subtract


def test_add():
    assert add(5, 3) == 10


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(5, 3) == 15