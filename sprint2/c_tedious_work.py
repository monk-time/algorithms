class Node:
    def __init__(self, value, next_item: 'Node' = None):
        self.value = value
        self.next_item = next_item


def solution(node: Node, pos_to_remove: int):
    if pos_to_remove == 0:
        return node.next_item
    new_head = node
    prev_node = node
    for _ in range(pos_to_remove):
        prev_node = node
        node = node.next_item
    prev_node.next_item = node.next_item
    return new_head # noqa
