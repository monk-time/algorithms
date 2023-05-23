def is_palindrome(s: str) -> bool:
    alphanums = list(filter(str.isalnum, s.lower()))
    return alphanums == alphanums[::-1]


if __name__ == '__main__':
    phrase = input()
    print(is_palindrome(phrase))
