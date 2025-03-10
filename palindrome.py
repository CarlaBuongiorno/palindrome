'''Write a function that takes a string, 
and returns True if that string is a palindrome.'''

def main():
    user_input = input("Type your palindrome: ")
    is_valid = check_if_valid(user_input)
    if is_valid:
        palindrome = is_palindrome(user_input)
    print(palindrome)


def check_if_valid(user_input):
    if not isinstance(user_input, str):
        raise TypeError('You have entered the wrong data type. A string is needed.')
    return user_input


def is_palindrome(user_input):
    pass


if __name__ == '__main__':
    main()