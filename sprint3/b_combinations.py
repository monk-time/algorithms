from itertools import product


BUTTONS = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}


def phone_combinations(s: str):
    pressed_buttons = (BUTTONS[ch] for ch in s)
    for comb in product(*pressed_buttons):
        yield ''.join(comb)


if __name__ == '__main__':
    s = input()
    print(*phone_combinations(s))
