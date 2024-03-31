"""ID посылки: 87911546."""

import operator

OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
}


class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()


def calc(expression: str) -> int:
    stack = Stack()
    for token in expression.split():
        if token not in OPERATIONS:
            stack.push(int(token))
            continue
        right, left = stack.pop(), stack.pop()
        stack.push(OPERATIONS[token](left, right))
    return stack.pop()


if __name__ == '__main__':
    print(calc(input()))
