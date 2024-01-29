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


def main():
    n = int(input())
    arr1 = [int(x) for x in input().split(' ') if len(x) > 0]
    m = int(input())
    arr2 = [int(x) for x in input().split(' ') if len(x) > 0]
    res_arr = [0] * (n + m)
    merge(arr1, arr2, res_arr)
    print(' '.join(map(str, res_arr)))


if __name__ == '__main__':
    main()