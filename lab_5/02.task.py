def is_palindrome(number):
    if str(number) == str(number)[::-1]:
        return 1
    return 0

number = int(input())
print(is_palindrome(number))