def find_path(filetree: list[str], filename: str) -> str:
    stack, prev_depth, prev_name = [], 0, None
    for s in filetree:
        name = s.strip()
        depth = len(s) - len(name)
        if depth > prev_depth:
            stack.append(prev_name)
        elif depth < prev_depth:
            for _ in range(prev_depth - depth):
                stack.pop()
        if name == filename:
            return (f'/{'/'.join(stack)}/' if stack else '/') + filename
        prev_depth = depth
        prev_name = name
    return ''


if __name__ == '__main__':
    filename = input()
    filetree = [input() for _ in range(int(input()))]
    print(find_path(filetree, filename))
