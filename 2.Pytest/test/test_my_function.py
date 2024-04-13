import pytest
import source.my_functions as my_functions

def test_add():
    assert my_functions.add(1, 2) == 3
    assert my_functions.add(1, 5) == 6

def test_add_strings():
    result = my_functions.add('hello', ' world!')
    assert result == 'hello world!'

def test_divide():
    assert my_functions.divide(10, 5) == 2

def test_divide_by_zero():
    with pytest.raises(ValueError):
        my_functions.divide(10, 0)

@pytest.mark.slow
def test_slow():
    assert my_functions.add(1, 2) == 3
    assert my_functions.add(1, 5) == 6

@pytest.mark.skip(reason="This feature is currently broken")
def test_skip():
    assert my_functions.add(1, 2) == 3
    assert my_functions.add(1, 5) == 6

@pytest.mark.xfail(reason="We know we cannot divide by zero")
def test_divide_by_zero():
    my_functions.divide(10, 0)