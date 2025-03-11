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

@pytest.mark.parametrize('user_input, expected', [
    ('a',                            True),
    ('aba',                          True),
    ('ab',                           False),
    ('a toyota',                     True),
    ('A Toyota',                     True),
    ('A Toyota\'s a Toyota',         True),
    ('Was it a car or a cat I saw?', True),
])
def test_palindrome(user_input, expected):
    assert is_palindrome(user_input) == expected
