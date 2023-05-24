class DequeSizeError(Exception):
    pass


class Deque:
    def __init__(self, max_size: int):
        self._max_size = max_size
        self._deque = [None] * max_size
        self._index_first = self._index_last = None
        self._size = 0

    def _check_full(self):
        if self._size == self._max_size:
            raise DequeSizeError()

    def _check_empty(self):
        if self._size == 0:
            raise DequeSizeError()

    def push_front(self, value: int):
        self._check_full()
        if self._size == 0:
            self._index_first = self._index_last = 0
        else:
            self._index_first = (self._index_first - 1) % self._max_size
        self._deque[self._index_first] = value
        self._size += 1

    def push_back(self, value: int):
        self._check_full()
        if self._size == 0:
            self._index_first = self._index_last = 0
        else:
            self._index_last = (self._index_last + 1) % self._max_size
        self._deque[self._index_last] = value
        self._size += 1

    def pop_front(self):
        self._check_empty()
        value = self._deque[self._index_first]
        self._index_first = (self._index_first + 1) % self._max_size
        self._size -= 1
        if self._size == 0:
            self._index_first = self._index_last = None
        return value  # noqa

    def pop_back(self):
        self._check_empty()
        value = self._deque[self._index_last]
        self._index_last = (self._index_last - 1) % self._max_size
        self._size -= 1
        if self._size == 0:
            self._index_first = self._index_last = None
        return value  # noqa


def execute(command: str, queue: Deque) -> None:
    method_name, *args = command.split()
    args = list(map(int, args))
    try:
        return_value = getattr(queue, method_name)(*args)
        if return_value is not None:
            print(return_value)
    except DequeSizeError:
        print('error')


if __name__ == '__main__':
    n = int(input())
    max_size = int(input())
    deque = Deque(max_size)
    for _ in range(n):
        command = input()
        execute(command, deque)
