def merge(arr1, arr2, general):
    p1 = 0
    p2 = 0
    g_p = 0
    while p1 < len(arr1) and p2 < len(arr2):
        if arr2[p2] < arr1[p1]:
            general[g_p] = arr2[p2]
            p2 += 1
        else:
            general[g_p] = arr1[p1]
            p1 += 1
        g_p += 1

    while p1 < len(arr1):
        general[g_p] = arr1[p1]
        p1 += 1
        g_p += 1

    while p2 < len(arr2):
        general[g_p] = arr2[p2]
        p2 += 1
        g_p += 1


def mergesort(arr):
    if len(arr) > 1:
        p = len(arr) // 2
        arr_l = arr[:p]
        arr_r = arr[p:]
        mergesort(arr_l)
        mergesort(arr_r)
        merge(arr_l, arr_r, arr)


def main():
    n = int(input())

    if n != 0:
        arr = [int(x) for x in input().split(' ')]
        mergesort(arr)
        print(' '.join(map(str, arr)))


if __name__ == '__main__':
    main()