from typing import List


def sift_down(heap: List[int], index: int) -> int:
    left = 2 * index
    right = left + 1
    if left >= len(heap):
        return index

    largest = right if right < len(heap) and heap[right] > heap[left] else left
    if heap[index] >= heap[largest]:
        return index

    heap[index], heap[largest] = heap[largest], heap[index]
    return sift_down(heap, largest)
