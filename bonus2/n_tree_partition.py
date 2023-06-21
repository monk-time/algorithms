from typing import Tuple

LOCAL = True

if LOCAL:

    class Node:
        def __init__(self, left=None, right=None, value=0, size=0):
            self.left = left
            self.right = right
            self.value = value
            self.size = size


def split(root, k) -> Tuple['Node', 'Node']:
    return Node(), Node()
