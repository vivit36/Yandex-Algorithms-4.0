def max_square(rows, columns, matrix):
    add_matrix = [[0 for y in range(columns + 1)] for x in range(rows + 1)]
    res = 0

    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == '1':
                add_matrix[i + 1][j + 1] = min(add_matrix[i][j], add_matrix[i + 1][j], add_matrix[i][j + 1]) + 1
                res = max(res, add_matrix[i + 1][j + 1])

    return res


def main():
    n, m = map(int, input().split())
    matrix = list()
    for i in range(n):
        matrix.append(input().split())

    print(max_square(n, m, matrix))


if __name__ == '__main__':
    main()
