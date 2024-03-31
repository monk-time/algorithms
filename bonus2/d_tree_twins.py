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


def solution(root1: Node | None, root2: Node | None) -> bool:
    """Check if two trees are identical."""
    return not any((root1, root2)) or (
        (root1 is not None and root2 is not None)
        and (root1.value == root2.value)
        and solution(root1.left, root2.left)
        and solution(root1.right, root2.right)
    )
