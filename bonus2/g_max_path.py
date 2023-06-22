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
    """Find a sum of the max path in a tree."""
    max_path = [root.value]

    def get_max_from_node(node: Optional[Node]):
        if node is None:
            return 0

        left_max = max(get_max_from_node(node.left), 0)
        right_max = max(get_max_from_node(node.right), 0)

        current_max_path = left_max + node.value + right_max
        max_path[0] = max(max_path[0], current_max_path)

        return node.value + max(left_max, right_max)

    get_max_from_node(root)
    return max_path[0]
