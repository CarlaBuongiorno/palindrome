def is_palindrome(user_input):
    cleaned_user_input = _clean_input(user_input)
    cleaned_user_input = list(cleaned_user_input)
    if cleaned_user_input != cleaned_user_input[::-1]:
        return False
    return True


def _clean_input(user_input): # private functions are not tested because they are an implementation detail of the public functions
    cleaned_input = user_input.replace(' ', '')
    print(cleaned_input)
    return cleaned_input
