from typing import Optional, Tuple


class Node:
    def __init__(
        self,
        left: Optional['Node'] = None,
        right: Optional['Node'] = None,
        value=0,
        size=0,
    ):
        self.left = left
        self.right = right
        self.value = value
        self.size = size


def split(
    root: Optional[Node], k: int
) -> Tuple[Optional[Node], Optional[Node]]:
    """Remove the smallest k nodes into a separate search tree."""
    if not root or k == 0:
        return None, root
    if k >= root.size:
        return root, None
    if not root.left:
        small_root = root
        small_root.right, root = split(root.right, k - 1)
        small_root.size -= root.size if root else 0
    elif root.left.size >= k:
        small_root, root.left = split(root.left, k)
        root.size -= k
    else:
        small_root = root
        small_root.right, root = split(root.right, k - root.left.size - 1)
        small_root.size -= root.size if root else 0
    return small_root, root
