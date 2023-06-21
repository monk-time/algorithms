LOCAL = True

if LOCAL:

    class Node:
        def __init__(self, left=None, right=None, value=0):
            self.left = left
            self.right = right
            self.value = value


def insert(root, key) -> 'Node':
    return Node()
