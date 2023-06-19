from typing import Iterable, List


def longest_balanced(strings: Iterable[str]) -> int:
    stack: List[str] = []
    max_sequence = ''
    for item in strings:
        prev, head = (
            (None, None)
            if not stack
            else (None, stack[-1])
            if len(stack) == 1
            else (stack[-2], stack[-1])
        )
        not_item = '1' if item == '0' else '0'
        if (not prev or prev == not_item) and (head and head == not_item):
            stack.pop()
            to_append = [head + item]
        elif (not prev or prev == item) and (
            head and len(head) > 1 and head[0] == item
        ):
            stack.pop()
            to_append = [item, head[1:] + item]
        elif (prev and head) and (
            (len(prev) > 1 and head == not_item)
            or (len(head) > 1 and prev == not_item)
        ):
            stack.pop()
            stack.pop()
            to_append = [prev + head + item]
        elif (prev and head) and (
            len(prev) > 1 and len(head) > 1 and prev[0] == not_item
        ):
            # TODO: разбить на два кейса?
            stack.pop()
            stack.pop()
            to_append = [prev + head, item]
        elif (prev and head) and (
            len(prev) > 1 and len(head) > 1 and prev[0] == item
        ):
            stack.pop()
            stack.pop()
            to_append = [item, prev[1:] + head + item]
        else:
            to_append = [item]
        # TODO: может, в кейсах --+ делать цикл?
        for new_item in to_append:
            stack.append(new_item)
            if len(new_item) > 1 and len(new_item) > len(max_sequence):
                max_sequence = new_item
    if len(stack) > 1 and len(stack[-1]) > 1 and len(stack[-2]) > 1:
        sequence = stack[-1] + stack[-2]
        if len(sequence) > len(max_sequence):
            max_sequence = sequence
    return len(max_sequence)


if __name__ == '__main__':
    # import random

    # while True:
    #     n = 3
    #     s = random.sample('01' * n, k=2 * n)
    #     if longest_balanced(s) != 2 * n:
    #         print(*s)
    #         raise Exception()

    from more_itertools import distinct_permutations

    n = 4
    for s in distinct_permutations('01' * n):
        if longest_balanced(s) != 2 * n:
            print(*s)
            print(f'got {longest_balanced(s)}, expected {2 * n}')
            raise Exception()

    # n = int(input())
    # strings = input().split()
    # print(longest_balanced(strings))
