from typing import List

Matrix = List[List[int]]


def parse_matrix(strs: List[str]) -> Matrix:
    return [list(map(int, s.split())) for s in strs]


def neighbors(matrix: Matrix, y: int, x: int) -> List[int]:
    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        x2, y2 = x + dx, y + dy
        if 0 <= x2 < cols and 0 <= y2 < rows:
            result.append(matrix[y2][x2])
    return sorted(result)


if __name__ == '__main__':
    rows = int(input())
    cols = int(input())
    matrix = parse_matrix(input() for _ in range(rows))
    x = int(input())
    y = int(input())
    result = neighbors(matrix, x, y)
    print(' '.join(map(str, result)))
