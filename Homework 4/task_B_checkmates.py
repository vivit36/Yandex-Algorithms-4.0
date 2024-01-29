def proverka(xy, coord):
    for i in range(len(coord) - 1):
        if xy[1] == coord[i][1] or abs(xy[0] - coord[i][0]) == abs(xy[1] - coord[i][1]):
            return False
    return True


def recursive(n, cnt=0, st=0, coord=[]):
    res = 0
    for i in range(st, n):
        for j in range(n):
            coord.append((i, j))
            cnt += 1
            if proverka((i, j), coord):
                if cnt == n:
                    res += 1
                else:
                    res += recursive(n, cnt, st + 1, coord)
            coord.pop()
            cnt -= 1
        return res


def main():
    n = int(input().strip())
    print(recursive(n))


if __name__ == '__main__':
    main()