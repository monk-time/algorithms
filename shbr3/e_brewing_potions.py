MAX_VALUE = 10**6


def make_ge_counter(
    a_sorted_desc: list[int], max_value: int = MAX_VALUE
) -> dict[int, int]:
    ge_counter = {}
    index = len(a_sorted_desc) - 1
    value = -max_value
    while index >= 0:
        while a_sorted_desc[index] >= value:
            ge_counter[value] = index + 1
            value += 1
        index -= 1
    while value <= max_value:
        ge_counter[value] = 0
        value += 1
    return ge_counter


def count_potions_ge_x(
    a: list[int], ge_counter: dict[int, int], x: int
) -> int:
    return sum(ge_counter[max(x - value, x)] for value in a)


def max_sum_quality(a: list[int], k: int) -> int:
    a_sorted_desc = sorted(a, reverse=True)
    ge_counter = make_ge_counter(a_sorted_desc)
    return 1


if __name__ == '__main__':
    a = [8, 8, 8, 5, 3, 0, 0, -1, -5, -5]
    print(make_ge_counter(a))

#     n, k = [int(s) for s in input().split()]
#     a = [int(s) for s in input().split()]
#     print(max_sum_quality(a, k))
