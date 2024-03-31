from itertools import product

LETTERS = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}


def phone_combinations(phone: str):
    yield from map(''.join, product(*map(LETTERS.get, phone)))  # type: ignore


def phone_combinations_rec(phone: str, prefix: str = ''):
    if len(prefix) == len(phone):
        yield prefix
        return
    for letter in LETTERS[phone[len(prefix)]]:
        yield from phone_combinations_rec(phone, prefix + letter)


if __name__ == '__main__':
    print(*phone_combinations(input()))
