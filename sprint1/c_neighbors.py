Matrix = list[list[int]]


def neighbors(matrix: Matrix, row: int, col: int) -> list[int]:
    rows = len(matrix)
    cols = len(matrix[0])
    deltas = ((-1, 0), (1, 0), (0, -1), (0, 1))
    coords = (tuple(map(sum, zip((row, col), d))) for d in deltas)
    in_range = lambda t: 0 <= t[0] < rows and 0 <= t[1] < cols
    get = lambda t: matrix[t[0]][t[1]]
    return sorted(map(get, filter(in_range, coords)))


if __name__ == '__main__':
    rows = int(input())
    cols = int(input())
    matrix = [list(map(int, input().split())) for _ in range(rows)]
    row = int(input())
    col = int(input())
    result = neighbors(matrix, row, col)
    print(' '.join(map(str, result)))
