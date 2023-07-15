def count_filled_blocks(heights: list[int]) -> int:
    def fill(left: int, right: int, step: int = 1) -> tuple[int, int]:
        total, cur_total, prev_max, prev_max_i = 0, 0, 0, -1
        for i in range(left, right + step, step):
            if prev_max > heights[i]:
                cur_total += prev_max - heights[i]
            else:
                total += cur_total
                cur_total = 0
                prev_max, prev_max_i = heights[i], i
        return total, prev_max_i

    total_ltr, max_i = fill(0, len(heights) - 1)
    if max_i == -1:
        return total_ltr
    total_rtl, _ = fill(len(heights) - 1, max_i, -1)
    return total_ltr + total_rtl


if __name__ == '__main__':
    input()
    heights = [int(s) for s in input().split()]
    print(count_filled_blocks(heights))
