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
    """Find sum of all path "numbers" in a tree."""

    def traverse(node: Optional[Node], prefix: str = ''):
        if not node:
            return
        new_prefix = prefix + str(node.value)
        if not node.left and not node.right:
            yield new_prefix
        yield from traverse(node.left, new_prefix)
        yield from traverse(node.right, new_prefix)

    return sum(map(int, traverse(root)))
