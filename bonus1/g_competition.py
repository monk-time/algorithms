from collections.abc import Sequence


def longest_balanced(sequence: Sequence[str]) -> int:
    balance = 0
    max_index = -1
    index_by_balance = {balance: max_index}
    max_length = 0

    for i, item in enumerate(sequence):
        balance += 1 if item == '1' else -1
        if balance not in index_by_balance:
            index_by_balance[balance] = i
            continue
        length = i - index_by_balance[balance]
        if length > max_length:
            max_length = length
            max_index = index_by_balance[balance] + 1

    return max_length


if __name__ == '__main__':
    n = int(input())
    strings = input().split()
    print(longest_balanced(strings))
