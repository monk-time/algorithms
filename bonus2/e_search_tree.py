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


def traverse(root: Optional[Node]):
    """Traverse all nodes in a tree in-order."""
    if not root:
        return
    yield from traverse(root.left)
    yield root
    yield from traverse(root.right)


def solution(root: Node) -> bool:
    """Check if a tree is a search tree."""
    nodes = traverse(root)
    prev_value = next(nodes).value
    for node in nodes:
        if node.value <= prev_value:
            return False
        prev_value = node.value
    return True
