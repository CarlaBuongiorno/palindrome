import pytest

from palindrome import (
    check_if_valid,
    is_palindrome,
    )


def test_function_exists():
    assert is_palindrome

def test_user_input_is_valid():
    assert check_if_valid('hello') == 'hello'

def test_user_input_not_valid():
    with pytest.raises(TypeError, match='You have entered the wrong data type. A string is needed.'):
        check_if_valid(123)

def test_is_palindrome():
    assert is_palindrome('a') == True

def test_is_palindrome_3_letters():
    assert is_palindrome('aba') == True

def test_not_a_palindrome():
    assert is_palindrome('ab') == False
