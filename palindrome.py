'''Find a palindrome.

Write a function that takes a string, 
and returns True if that string is a palindrome.'''

from pure_palindrome import is_palindrome


def main():
    user_input = input("Type your palindrome: ")
    palindrome = is_palindrome(user_input)
    print(palindrome)


if __name__ == '__main__':
    main()