from collections import deque


class MyQueueSizedDeque:
    def __init__(self, max_size: int):
        self.max_size = max_size
        self._queue = deque()

    def push(self, value: int):
        if self.size() >= self.max_size:
            return 'error'
        self._queue.appendleft(value)
        return None

    def pop(self):
        if not self._queue:
            return 'None'
        return self._queue.pop()

    def peek(self):
        if not self._queue:
            return 'None'
        return self._queue[-1]

    def size(self):
        return len(self._queue)


class MyQueueSized:
    def __init__(self, max_size: int):
        self.max_size = max_size
        self.queue = [None] * max_size
        self.index_first = self.index_last = 0
        self.queue_size = 0

    def push(self, value: int):
        if self.queue_size >= self.max_size:
            return 'error'
        self.queue[self.index_last] = value
        self.index_last = (self.index_last + 1) % self.max_size
        self.queue_size += 1
        return None

    def pop(self):
        if not self.queue_size:
            return 'None'
        value = self.queue[self.index_first]
        self.index_first = (self.index_first + 1) % self.max_size
        self.queue_size -= 1
        return value  # noqa

    def peek(self):
        if not self.queue_size:
            return 'None'
        return self.queue[self.index_first]

    def size(self):
        return self.queue_size


def execute(command: str, queue: MyQueueSized) -> None:
    method_name, *args = command.split()
    args = list(map(int, args))
    return_value = getattr(queue, method_name)(*args)
    if return_value is not None:
        print(return_value)


if __name__ == '__main__':
    n = int(input())
    max_size = int(input())
    queue = MyQueueSized(max_size)
    for _ in range(n):
        command = input()
        execute(command, queue)
