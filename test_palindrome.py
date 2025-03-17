import pytest

from pure_palindrome import is_palindrome


def test_function_exists():
    assert is_palindrome


def test_valid_user_input():
    with pytest.raises(TypeError):
        is_palindrome(123)


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
