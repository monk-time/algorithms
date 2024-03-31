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


def traverse(root: Node | None):
    """Traverse all nodes in a tree in-order."""
    if not root:
        return
    yield from traverse(root.left)
    yield root
    yield from traverse(root.right)


def traverse_iter(root: Node | None):
    """Traverse all nodes in a tree in-order (without recursion)."""
    stack, node = [], root
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            yield node
            node = node.right


def solution(root: Node) -> bool:
    """Check if a tree is a search tree."""
    it, it2 = traverse(root), traverse(root)
    next(it2, None)
    return all(left.value < right.value for left, right in zip(it, it2))


def solution2(root: Node) -> bool:
    def rec(root: Node):
        is_left_ok, left_min, left_max = (
            rec(root.left) if root.left else (True, root.value, -float('inf'))
        )
        is_right_ok, right_min, right_max = (
            rec(root.right) if root.right else (True, float('inf'), root.value)
        )
        is_root_ok = (
            is_left_ok and is_right_ok and left_max < root.value < right_min
        )
        return is_root_ok, left_min, right_max

    return rec(root)[0]
