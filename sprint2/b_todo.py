class Node:
    def __init__(self, value, next_item: 'Node | None' = None):
        self.value = value
        self.next_item = next_item


def print_linked_list(node: Node | None):
    while node:
        print(node.value)
        node = node.next_item


if __name__ == '__main__':
    n = int(input())
    node = None
    for _ in range(n):
        node = Node(value=input(), next_item=node)
    print_linked_list(node)
