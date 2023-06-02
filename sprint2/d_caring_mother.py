from itertools import count


class Node:
    def __init__(self, value, next_item: 'Node' = None):
        self.value = value
        self.next_item = next_item


def find(node: Node, value):
    i = 0
    while node:
        if node.value == value:
            return i
        node = node.next_item
        i += 1
    return -1


def find_iter(head: Node, value):
    def node_iter(node):
        while node:
            yield node
            node = node.next_item

    enumerated = zip(count(), node_iter(head))
    return next((i for i, node in enumerated if node.value == value), -1)


if __name__ == '__main__':
    n = int(input())
    node = None
    for _ in range(n):
        node = Node(value=input(), next_item=node)
    value = input()
    print(find(node, value))
