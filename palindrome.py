'''Write a function that takes a string, 
and returns True if that string is a palindrome.'''

def main():
    user_input = input("Type your palindrome: ")
    # user_input = 1
    try:
        check_if_valid(user_input)
        palindrome = is_palindrome(user_input)
        print(palindrome)
    except TypeError as e:
        print(e)


def check_if_valid(user_input):
    if not isinstance(user_input, str):
        raise TypeError('You have entered the wrong data type. A string is needed.')
    return user_input


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


if __name__ == '__main__':
    main()