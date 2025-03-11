def is_palindrome(user_input):
    cleaned_user_input = _clean_input(user_input)
    if cleaned_user_input != cleaned_user_input[::-1]:
        return False
    return True


def _clean_input(user_input): # private functions are not tested because they are an implementation detail of the public functions
    return list(user_input.replace(' ', '').lower())
