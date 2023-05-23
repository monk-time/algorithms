from typing import List

Matrix = List[List[int]]


def transpose(matrix: Matrix) -> Matrix:
    rows = len(matrix)
    cols = len(matrix[0])
    return [[matrix[i][j] for i in range(rows)] for j in range(cols)]


if __name__ == '__main__':
    rows = int(input())
    cols = int(input())
    matrix = [[int(s) for s in input().split()] for _ in range(rows)]
    transposed = transpose(matrix)
    for row in transposed:
        print(' '.join(map(str, row)))
