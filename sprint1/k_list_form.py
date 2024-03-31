ListForm = list[int]


def parse(s: str) -> ListForm:
    return [int(ch) for ch in s.split()]


def to_digits(n: int) -> ListForm:
    return [int(ch) for ch in str(n)]


def from_digits(a: ListForm) -> int:
    return int(''.join(map(str, a)))


def special_sum(x: ListForm, k: int) -> ListForm:
    return to_digits(from_digits(x) + k)


if __name__ == '__main__':
    n = int(input())
    x = parse(input())
    k = int(input())
    print(' '.join(map(str, special_sum(x, k))))
