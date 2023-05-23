def to_binary(n: int) -> str:
    if n == 0:
        return '0'
    result = ''
    while n:
        result += str(n % 2)
        n //= 2
    return result[::-1]


if __name__ == '__main__':
    n = int(input())
    print(to_binary(n))
