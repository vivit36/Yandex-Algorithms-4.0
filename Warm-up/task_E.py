def discontent(n, arr):
    res = list()
    for el in arr:
        tmp = 0
        for sub in arr:
            tmp += abs(el - sub)
        res.append(tmp)

    return res


def discontent2(n, arr):
    pref_sum = [0] * n
    post_sum = [0] * n

    for i in range(1, n):
        pref_sum[i] = (arr[i] - arr[i - 1]) * i + pref_sum[i - 1]

    for i in range(n-2, -1, -1):
        post_sum[i] = (arr[i + 1] - arr[i]) * (n - (i + 1)) + post_sum[i + 1]

    return list(map(sum, zip(pref_sum, post_sum)))


def main():
    n = int(input())
    arr = [int(x) for x in input().split(' ')]
    res = discontent2(n, arr)
    for el in res:
        print(el, end=' ')


if __name__ == '__main__':
    main()