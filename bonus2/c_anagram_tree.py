from typing import Optional


class Node:
    def __init__(
        self,
        value,
        left: Optional['Node'] = None,
        right: Optional['Node'] = None,
    ):
        self.value = value
        self.left = left
        self.right = right


def solution(root: Node) -> bool:
    """Check if a tree is an anagram tree, i.e. vertically symmetric."""
    layer = [root]
    while any(layer):
        next_layer, values = [], []
        for node in layer:
            next_layer += [node.left, node.right] if node else [None, None]
            values += [
                node.left.value if node and node.left else None,
                node.right.value if node and node.right else None,
            ]
        if values != values[::-1]:
            return False
        layer = next_layer
    return True
