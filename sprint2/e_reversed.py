class DoubleConnectedNode:
    def __init__(
        self,
        value,
        next: 'DoubleConnectedNode' = None,
        prev: 'DoubleConnectedNode' = None,
    ):
        self.value = value
        self.next = next
        self.prev = prev


def solution(node: DoubleConnectedNode):
    prev_node = node
    while node:
        node.prev, node.next = node.next, node.prev
        prev_node = node
        node = node.prev
    return prev_node
