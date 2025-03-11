import re


def is_palindrome(user_input):
    cleaned_user_input = _clean_input(user_input)
    return cleaned_user_input == cleaned_user_input[::-1]


def _clean_input(user_input): # private functions are not tested because they are an implementation detail of the public functions
    '''Find all characters that are not letters or numbers,
    and replace them with an empty string.'''
    pattern = r'[^a-zA-Z0-9]'
    return list(re.sub(pattern, '', user_input.lower()))
