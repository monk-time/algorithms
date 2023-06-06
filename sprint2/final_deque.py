"""ID посылки: 87911435."""


class DequeFullError(Exception):
    pass


class DequeEmptyError(Exception):
    pass


class Deque:
    def __init__(self, max_size: int):
        self._max_size = max_size
        self._deque = [None] * max_size
        self._first = 1
        self._last = 0
        self._size = 0

    def _check_full(self):
        if self._size == self._max_size:
            raise DequeFullError('Max deque size reached')

    def _check_empty(self):
        if self._size == 0:
            raise DequeEmptyError('Deque is empty')

    def push_front(self, value: int):
        self._check_full()
        self._first = (self._first - 1) % self._max_size
        self._deque[self._first] = value
        self._size += 1

    def push_back(self, value: int):
        self._check_full()
        self._last = (self._last + 1) % self._max_size
        self._deque[self._last] = value
        self._size += 1

    def pop_front(self):
        self._check_empty()
        value = self._deque[self._first]
        self._first = (self._first + 1) % self._max_size
        self._size -= 1
        return value  # noqa

    def pop_back(self):
        self._check_empty()
        value = self._deque[self._last]
        self._last = (self._last - 1) % self._max_size
        self._size -= 1
        return value  # noqa


def main():
    command_count = int(input())
    max_size = int(input())
    deque = Deque(max_size)
    for _ in range(command_count):
        method_name, *method_args = input().split()
        method_args = map(int, method_args)
        try:
            return_value = getattr(deque, method_name)(*method_args)
            if return_value is not None:
                print(return_value)
        except (DequeFullError, DequeEmptyError):
            print('error')


if __name__ == '__main__':
    main()
