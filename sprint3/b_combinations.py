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


def phone_combinations_rec(buttons: str, acc: str = ''):
    if len(acc) == len(buttons):
        yield acc
        return
    for letter in LETTERS[buttons[len(acc)]]:
        yield from phone_combinations_rec(buttons, acc + letter)


if __name__ == '__main__':
    print(*phone_combinations(input()))
