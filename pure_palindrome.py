import re


def is_palindrome(user_input):
    _check_if_valid(user_input)
    cleaned_user_input = _clean_input(user_input)
    return cleaned_user_input == cleaned_user_input[::-1]


def _check_if_valid(user_input):
    if not isinstance(user_input, str):
        raise TypeError('You have entered the wrong data type. A string is needed.')


def _clean_input(user_input): # private functions are not tested because they are an implementation detail of the public functions
    '''Only letters and numbers are considered for a palindrome.

    Find all characters that are not letters or numbers,
    and replace them with an empty string.'''
    pattern = r'[^a-zA-Z0-9]'
    return list(re.sub(pattern, '', user_input.lower()))
