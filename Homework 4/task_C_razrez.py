import math


def grey(cnt):
    bin_cnt = cnt + 1
    grey = bin_cnt ^ (bin_cnt >> 1)
    tmp = (cnt ^ (cnt >> 1)) ^ grey
    pos = int(math.log2(tmp))

    if bin(grey)[-(pos + 1)] == '0':
        return None, pos + 1
    else:
        return pos + 1, None


def razrez_v2(matr):
    n = len(matr)
    vertexes = {x + 1 for x in range(n)}
    max_razr = 0
    save_cnt = -1

    big_sum = 0

    first_set = set()
    second_set = vertexes

    for cnt in range(0, 2 ** n // 2 - 1):
        add_vertex, del_vertex = grey(cnt)

        if add_vertex is not None:
            first_set.add(add_vertex)
            second_set.remove(add_vertex)
        if del_vertex is not None:
            first_set.remove(del_vertex)
            second_set.add(del_vertex)


        cur_razr = 0

        if add_vertex is not None:
            for i in second_set:
                cur_razr += matr[add_vertex - 1][i - 1]
            for i in first_set:
                cur_razr -= matr[add_vertex - 1][i - 1]
        if del_vertex is not None:
            for i in first_set:
                cur_razr += matr[del_vertex - 1][i - 1]
            for i in second_set:
                cur_razr -= matr[del_vertex - 1][i - 1]

        big_sum = big_sum + cur_razr
        if big_sum > max_razr:
            max_razr = big_sum
            save_cnt = cnt + 1

    return max_razr, save_cnt


def main():
    n = int(input().strip())
    matr = list()
    for i in range(n):
        row = [int(x) for x in input().strip().split()]
        matr.append(row)

    max_value, save_cnt = razrez_v2(matr)
    save_cnt = (save_cnt ^ (save_cnt >> 1)) ^ (2 ** n - 1)
    print(max_value)
    res = list()

    while save_cnt != 0:
        if save_cnt % 2 == 1:
            res.append('1')
        else:
            res.append('2')
        save_cnt = save_cnt // 2
    print(' '.join(res))


if __name__ == '__main__':
    main()