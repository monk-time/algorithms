def gen_binary(n, prefix, space=''):
    if n == 0:
        print(f"{space}└───print('{prefix}')")
    else:
        print(f"{space}├───gen_binary({n - 1}, '{prefix}left ')")
        gen_binary(n - 1, prefix + 'left ', space + '│   ')
        print(f"{space}└───gen_binary({n - 1}, '{prefix}right ')")
        gen_binary(n - 1, prefix + 'right ', space + '    ')


if __name__ == '__main__':
    print("gen_binary(3, '')")
    gen_binary(3, '')
