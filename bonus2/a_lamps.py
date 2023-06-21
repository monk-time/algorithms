LOCAL = True

if LOCAL:

    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right


def solution(root) -> int:
    return 1
