from typing import Optional


class Node:
    def __init__(
        self,
        left: Optional['Node'] = None,
        right: Optional['Node'] = None,
        value=0,
    ):
        self.left = left
        self.right = right
        self.value = value


def print_range(node: Node | None, left, right):
    """Print all nodes in a search tree that are in a given range."""
    if not node:
        return
    if node.value >= left:
        print_range(node.left, left, right)
    if left <= node.value <= right:
        print(node.value)
    if node.value <= right:
        print_range(node.right, left, right)
