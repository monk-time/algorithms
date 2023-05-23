from collections import deque


class ListQueueDeque:
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


class Node:
    def __init__(self, value, next_item: 'Node' = None):
        self.value = value
        self.next_item = next_item


class ListQueue:
    def __init__(self):
        self.first = self.last = None
        self.queue_size = 0

    def put(self, value: int):
        node = Node(value)
        if not self.first:
            self.first = node
        else:
            self.last.next_item = node
        self.last = node
        self.queue_size += 1

    def get(self):
        if not self.first:
            return 'error'
        if not self.first.next_item:
            self.last = None
        value = self.first.value
        self.first = self.first.next_item
        self.queue_size -= 1
        return value  # noqa

    def size(self):
        return self.queue_size


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
