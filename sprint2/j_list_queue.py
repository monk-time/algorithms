from collections import deque


class ListQueue:
    def __init__(self):
        self._queue = deque()

    def put(self, value: int):
        self._queue.appendleft(value)

    def get(self):
        if not self._queue:
            return 'error'
        return self._queue.pop()

    def size(self):
        return len(self._queue)


def execute(command: str, queue: ListQueue) -> None:
    method_name, *args = command.split()
    args = list(map(int, args))
    return_value = getattr(queue, method_name)(*args)
    if return_value is not None:
        print(return_value)


if __name__ == '__main__':
    n = int(input())
    queue = ListQueue()
    for _ in range(n):
        command = input()
        execute(command, queue)
