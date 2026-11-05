from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(9, 7) == 2

def test_multiply():
    assert multiply(3, 8) == 24

def test_divide():
    assert divide(6, 2) == 3

def test_negative_add():
    assert add(-6, -1) == -7

def test_negative_multiply():
    assert multiply(-5, 3) == -15

def test_uneven_divide():
    assert divide(5, 2) == 2.5
