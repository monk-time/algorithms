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


def solution(root: Node | None) -> int:
    """Find max depth of a tree."""
    if not root:
        return 0
    return 1 + max(solution(root.left), solution(root.right))
