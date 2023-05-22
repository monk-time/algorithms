def is_power_of_four(n: int) -> bool:
    while n % 4 == 0:
        n //= 4
    return n == 1


if __name__ == '__main__':
    n = int(input())
    print(is_power_of_four(n))
