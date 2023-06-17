from typing import List


def count_max_blocks(a: List[int]) -> int:
    blocks = []
    for n in a:
        cur_min, cur_max = n, n
        while blocks:
            prev_min, prev_max = blocks[-1]
            if prev_max <= cur_min:
                break
            blocks.pop()
            cur_min = min(prev_min, cur_min)
            cur_max = max(prev_max, cur_max)
        blocks.append((cur_min, cur_max))
    return len(blocks)


if __name__ == '__main__':
    _ = int(input())
    nums = list(map(int, input().split()))
    print(count_max_blocks(nums))
