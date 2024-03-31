Matrix = list[list[int]]


def transpose(matrix: Matrix, rows: int, cols: int) -> Matrix:
    return [[matrix[i][j] for i in range(rows)] for j in range(cols)]


if __name__ == '__main__':
    rows = int(input())
    cols = int(input())
    matrix = [[int(s) for s in input().split()] for _ in range(rows)]
    transposed = transpose(matrix, rows, cols)
    for row in transposed:
        print(' '.join(map(str, row)))
