def partition(arr, l, r, x):
    e_p, g_p, n_p = 0, 0, 0

    while n_p != len(arr):
        if arr[n_p] < x:
            tmp = arr[n_p]
            arr[n_p] = arr[g_p]
            arr[g_p] = arr[e_p]
            arr[e_p] = tmp
            n_p += 1
            g_p += 1
            e_p += 1
        elif arr[n_p] == x:
            tmp = arr[n_p]
            arr[n_p] = arr[g_p]
            arr[g_p] = tmp
            n_p += 1
            g_p += 1
        else:
            n_p += 1

    return e_p


def main():
    n = int(input())
    arr = [int(x) for x in input().split(' ') if len(x) > 0]
    x = int(input())
    p = partition(arr, 0, n - 1, x)
    print(p)
    print(n - p)


if __name__ == '__main__':
    main()