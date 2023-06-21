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


def insert(root: Node, key) -> Node:
    """Insert a node into a search tree."""
    node = root
    while node:
        if key < node.value:
            if not node.left:
                node.left = Node(None, None, key)
                break
            node = node.left
        else:
            if not node.right:
                node.right = Node(None, None, key)
                break
            node = node.right
    return root
