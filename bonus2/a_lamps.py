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


def solution(root: Node) -> int:
    """DFS for max value in a tree."""
    stack, max_value = [root], root.value
    while stack:
        node = stack.pop()
        max_value = max(node.value, max_value)
        for child in (node.left, node.right):
            if child:
                stack.append(child)
    return max_value
