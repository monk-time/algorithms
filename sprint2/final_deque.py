"""ID посылки: 87898143."""


class DequeSizeError(Exception):
    pass


class Deque:
    def __init__(self, max_size: int):
        self._max_size = max_size
        self._deque = [None] * max_size
        self._head = self._tail = 0
        self._size = 0

    def _check_full(self):
        if self._size == self._max_size:
            raise DequeSizeError('Max deque size reached')

    def _check_empty(self):
        if self._size == 0:
            raise DequeSizeError('Deque is empty')

    def push_front(self, value: int):
        self._check_full()
        self._head = (self._head - 1) % self._max_size
        self._deque[self._head] = value
        self._size += 1

    def push_back(self, value: int):
        self._check_full()
        self._deque[self._tail] = value
        self._tail = (self._tail + 1) % self._max_size
        self._size += 1

    def pop_front(self):
        self._check_empty()
        value = self._deque[self._head]
        self._head = (self._head + 1) % self._max_size
        self._size -= 1
        return value  # noqa

    def pop_back(self):
        self._check_empty()
        self._tail = (self._tail - 1) % self._max_size
        value = self._deque[self._tail]
        self._size -= 1
        return value  # noqa


def main():
    n = int(input())
    max_size = int(input())
    deque = Deque(max_size)
    for _ in range(n):
        method_name, *args = input().split()
        args = map(int, args)
        try:
            return_value = getattr(deque, method_name)(*args)
            if return_value is not None:
                print(return_value)
        except DequeSizeError:
            print('error')


if __name__ == '__main__':
    main()
