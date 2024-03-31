def gen_binary(n, prefix, space=''):
    if n == 0:
        print(f"{space}└───print('{prefix}')")
    else:
        print(f"{space}├───gen_binary({n - 1}, '{prefix}0 ')")
        gen_binary(n - 1, prefix + '0', space + '│   ')
        print(f"{space}└───gen_binary({n - 1}, '{prefix}1')")
        gen_binary(n - 1, prefix + '1', space + '    ')


def gen_brackets(n: int, left: int = 0, right: int = 0, s: str = '', space=''):
    if left == right == n:
        print(f'{space}└───print: {s}')
    if left < n:
        div = '├' if right < left else '└'
        print(f"{space}{div}───gen_brackets({n}, {left + 1}, {right}, '{s}(')")
        div = '│' if right < left else ' '
        gen_brackets(n, left + 1, right, f'{s}(', space + f'{div}   ')
    if right < left:
        print(f"{space}└───gen_brackets({n}, {left}, {right + 1}, '{s})')")
        gen_brackets(n, left, right + 1, f'{s})', space + '    ')


if __name__ == '__main__':
    # print("gen_binary(3, '')")
    # gen_binary(3, '')
    print("gen_brackets(3, '')")
    gen_brackets(3)
