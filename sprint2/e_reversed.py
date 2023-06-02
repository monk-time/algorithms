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


def print_linked_list(node: DoubleConnectedNode):
    while node:
        print(node.value)
        node = node.next


def reverse(node: DoubleConnectedNode):
    prev_node = node
    while node:
        node.prev, node.next = node.next, node.prev
        prev_node = node
        node = node.prev
    return prev_node


if __name__ == '__main__':
    n = int(input())
    head = node = prev_node = None
    for _ in range(n):
        node = DoubleConnectedNode(value=input(), prev=prev_node)
        if not head:
            head = node
        if prev_node:
            prev_node.next = node
        prev_node = node
    head = reverse(head)
    print_linked_list(head)
