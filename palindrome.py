'''Write a function that takes a string, 
and returns True if that string is a palindrome.'''

from pure_palindrome import is_palindrome

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


if __name__ == '__main__':
    main()