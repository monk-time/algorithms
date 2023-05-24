OPERATIONS = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b,
}


def calc(expression: str) -> int:
    stack = []
    for s in expression.split():
        if s not in OPERATIONS:
            stack.append(int(s))
            continue
        b, a = stack.pop(), stack.pop()
        stack.append(OPERATIONS[s](a, b))
    return stack.pop()


if __name__ == '__main__':
    expression = input()
    print(calc(expression))
