from pathlib import Path


def get_canonical_path_cheat(s: str) -> str:
    return str(Path(s).resolve())


def get_canonical_path(s: str) -> str:
    parts = []
    for part in s.split('/'):
        match part:
            case '' | '.':
                pass
            case '..':
                if parts:
                    parts.pop()
            case _:
                parts.append(part)
    return '/' + '/'.join(parts)


if __name__ == '__main__':
    path = input()
    print(get_canonical_path(path))
