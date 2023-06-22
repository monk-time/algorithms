from typing import List


def sift_up(heap: List[int], index: int) -> int:
    if index == 1:
        return index

    parent = index // 2
    if heap[parent] >= heap[index]:
        return index

    heap[parent], heap[index] = heap[index], heap[parent]
    return sift_up(heap, parent)
