from itertools import count


class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def solution(node: Node, value):
    i = 0
    while node:
        if node.value == value:
            return i
        node = node.next_item
        i += 1
    return -1


def solution_iter(head: Node, value):
    def node_iter(node):
        while node:
            yield node
            node = node.next_item

    enumerated = zip(count(), node_iter(head))
    return next((i for i, node in enumerated if node.value == value), -1)
