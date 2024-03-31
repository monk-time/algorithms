from typing import Optional


class Node:
    def __init__(self, value: int, parent: Optional['Node'] = None):
        self.value = value
        self.parent = parent
        self.depth = parent.depth + 1 if parent else 1


def make_tree(parent_values: list[int]) -> list[Node]:
    nodes = [Node(0)]
    visited: set[Node] = set()
    for i, parent_value in enumerate(parent_values):
        parent = nodes[parent_value]
        visited.add(parent)
        node = Node(i + 1, parent)
        nodes.append(node)
    return [node for node in nodes if node not in visited]


def max_depth(leaves: list[Node]) -> int:
    index, _ = max(enumerate(leaves), key=lambda t: t[1].depth)
    return leaves[index].value


if __name__ == '__main__':
    n = int(input())
    parent_values = [int(input()) for _ in range(n)]
    leaves = make_tree(parent_values)
    print(max_depth(leaves))
