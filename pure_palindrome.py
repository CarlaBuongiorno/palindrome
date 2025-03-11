def is_palindrome(user_input):
    cleaned_user_input = _clean_input(user_input)
    return cleaned_user_input == cleaned_user_input[::-1]


def _clean_input(user_input): # private functions are not tested because they are an implementation detail of the public functions
    return list(user_input.replace(' ', '').lower())
