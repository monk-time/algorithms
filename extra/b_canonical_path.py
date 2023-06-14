from pathlib import Path


def get_canonical_path_cheat(s: str) -> str:
    return str(Path(s).resolve())


def get_canonical_path(s: str) -> str:
    parts = []
    for part in s.split('/'):
        if part == '..' and parts:
            parts.pop()
        elif part not in ('', '.', '..'):
            parts.append(part)
    return '/' + '/'.join(parts)


if __name__ == '__main__':
    path = input()
    print(get_canonical_path(path))
