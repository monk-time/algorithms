"""ID посылки: 87897803."""


OPERATIONS = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b,
}


def calc(expression: str) -> int:
    stack = []
    for token in expression.split():
        if token not in OPERATIONS:
            stack.append(int(token))
            continue
        b, a = stack.pop(), stack.pop()
        stack.append(OPERATIONS[token](a, b))
    return stack[-1]


if __name__ == '__main__':
    print(calc(input()))
