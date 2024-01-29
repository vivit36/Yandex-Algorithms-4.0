import itertools


def kommi(matr, n, min_len):
    vertexes = {x for x in range(2, n + 1)}
    best_way = float('inf')

    for perm in itertools.permutations(vertexes):
        path = [1] + list(perm) + [n + 1]
        cur_way = 0
        valid = True
        for i in range(n):
            dist = matr[path[i] - 1][path[i + 1] - 1]
            if dist != 0 and cur_way + min_len[path[i]] < best_way:
                cur_way += dist
            else:
                valid = False
                break

        if valid is True and cur_way < best_way:
            best_way = cur_way

    return best_way if best_way != float('inf') else -1


def main():
    n = int(input().strip())
    if n == 1:
        print('0')
    else:
        min_len = dict()
        matr = [[] for _ in range(n + 1)]

        for i in range(n):
            row = [int(x) for x in input().strip().split()]
            min_len[i + 1] = min([t for t in row if t > 0])
            row.append(row[0])
            matr[i] = row

        matr[n] = matr[0]

        print(kommi(matr, n, min_len))


if __name__ == '__main__':
    main()