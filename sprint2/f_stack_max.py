class StackMax:
    def __init__(self):
        self._stack = []
        self._max = []

    def push(self, value: int):
        self._stack.append(value)
        if not self._max or value >= self._max[-1]:
            self._max.append(value)

    def pop(self):
        if not self._stack:
            return 'error'
        value = self._stack.pop()
        if self._max[-1] == value:
            self._max.pop()
        return None

    def get_max(self):
        if not self._max:
            return 'None'
        return self._max[-1]


def execute(command: str, stack: StackMax) -> None:
    method_name, *args = command.split()
    args = list(map(int, args))
    return_value = getattr(stack, method_name)(*args)
    if return_value is not None:
        print(return_value)


if __name__ == '__main__':
    n = int(input())
    stack = StackMax()
    for _ in range(n):
        command = input()
        execute(command, stack)
