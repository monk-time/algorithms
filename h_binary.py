def binary_sum(a: str, b: str) -> str:
    result = ''
    carry_over = 0
    for i in range(1, max(len(a), len(b)) + 1):
        left = a[-i] if i <= len(a) else '0'
        right = b[-i] if i <= len(b) else '0'
        pos_sum = int(left) + int(right) + carry_over
        carry_over, digit = divmod(pos_sum, 2)
        result += str(digit)
    if carry_over:
        result += '1'
    return result[::-1]


if __name__ == '__main__':
    a = input()
    b = input()
    print(binary_sum(a, b))
