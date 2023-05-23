class Node:
    def __init__(self, value, next_item: 'Node' = None):
        self.value = value
        self.next_item = next_item


def solution(node):
    while node:
        print(node.value)
        node = node.next_item
