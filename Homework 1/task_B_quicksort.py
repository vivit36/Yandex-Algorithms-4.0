import random


def partition(arr, l, r, x):
    e_p, g_p, n_p = l, l, l

    while n_p != r + 1:
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

    return e_p, g_p


def my_quicksort(arr, l, r):
    if l < r:
        x = arr[random.randint(l, r)]
        p = partition(arr, l, r, x)
        my_quicksort(arr, l, p[0] - 1)
        my_quicksort(arr, p[1], r)


def main():
    n = int(input())

    if n != 0:
        arr = [int(x) for x in input().split(' ') if len(x) > 0]
        my_quicksort(arr, 0, n - 1)
        for el in arr:
            print(el, end=' ')


if __name__ == '__main__':
    main()