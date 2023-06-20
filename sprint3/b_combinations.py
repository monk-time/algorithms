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


def phone_combinations(buttons: str):
    pressed_buttons = (LETTERS[b] for b in buttons)
    for comb in product(*pressed_buttons):
        yield ''.join(comb)


def phone_combinations_rec(buttons: str, prefix: str = ''):
    if len(prefix) == len(buttons):
        yield prefix
        return
    for letter in LETTERS[buttons[len(prefix)]]:
        yield from phone_combinations_rec(buttons, prefix + letter)


def phone_combinations_rec_simple(buttons: str, prefix: str = ''):
    if len(prefix) == len(buttons):
        print(prefix)
    else:
        letters = LETTERS[buttons[len(prefix)]]
        phone_combinations_rec_simple(buttons, prefix + letters[0])
        phone_combinations_rec_simple(buttons, prefix + letters[1])
        phone_combinations_rec_simple(buttons, prefix + letters[2])


if __name__ == '__main__':
    print(*phone_combinations(input()))
