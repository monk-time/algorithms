class Node:
    def __init__(self, value, next_item: 'Node' = None):
        self.value = value
        self.next_item = next_item


def print_linked_list(node: Node):
    while node:
        print(node.value)
        node = node.next_item


def remove(node: Node, pos_to_remove: int):
    if pos_to_remove == 0:
        return node.next_item
    head = prev_node = node
    for _ in range(pos_to_remove):
        prev_node = node
        node = node.next_item
    prev_node.next_item = node.next_item
    return head  # noqa


if __name__ == '__main__':
    n = int(input())
    node = None
    for _ in range(n):
        node = Node(value=input(), next_item=node)
    pos_to_remove = int(input())
    node = remove(node, pos_to_remove)
    print_linked_list(node)
