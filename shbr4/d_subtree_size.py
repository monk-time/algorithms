from typing import Iterable


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


Nodes = list[Node]


def traverse_preorder(node: Node) -> Iterable[Node]:
    stack = [node]
    while stack:
        node = stack.pop()
        yield node
        stack.extend(reversed(node.children))


def traverse_postorder(node: Node) -> Iterable[Node]:
    stack = [node]
    visited = set()
    while stack:
        node = stack.pop()
        if node in visited:
            yield node
            continue
        stack.append(node)
        stack.extend(reversed(node.children))
        visited.add(node)


def create_directed_tree(vertice_count: int, edges: list[list[int]]) -> Nodes:
    nodes = [Node(key) for key in range(1, vertice_count + 1)]
    for left, right in edges:
        left_node, right_node = nodes[left - 1], nodes[right - 1]
        left_node.children.append(right_node)
        right_node.children.append(left_node)
    for node in traverse_preorder(nodes[0]):
        for child in node.children:
            child.children.remove(node)
    return nodes


def subtree_sizes(nodes: Nodes) -> list[int]:
    sizes = [0] * len(nodes)
    for node in traverse_postorder(nodes[0]):
        sizes[node.value - 1] = 1 + sum(
            sizes[child.value - 1] for child in node.children
        )
    return sizes


if __name__ == '__main__':
    vertice_count = int(input())
    edges = [
        [int(s) for s in input().split()] for _ in range(vertice_count - 1)
    ]
    nodes = create_directed_tree(vertice_count, edges)
    print(*subtree_sizes(nodes), sep=' ')
