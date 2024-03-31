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
    def balanced_depth(root: Node | None):
        """Return binary tree depth if it's balanced, -1 otherwise."""
        if not root:
            return 0

        left_depth = balanced_depth(root.left)
        if left_depth == -1:
            return -1
        right_depth = balanced_depth(root.right)
        if right_depth == -1:
            return -1

        if abs(left_depth - right_depth) > 1:
            return -1
        return max(left_depth, right_depth) + 1

    return balanced_depth(root) != -1
