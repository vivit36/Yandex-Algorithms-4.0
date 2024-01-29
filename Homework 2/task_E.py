def is_eq_double(h_1, x, h_2, p, from1, from2, slen):
    return (
        (h_1[from1 + slen - 1] + h_2[from2 - 1] * x[slen]) % p ==
        (h_2[from2 + slen - 1] + h_1[from1 - 1] * x[slen]) % p
    )


def bin_search_2(h_1, x, h_2, p, from1, from2, len_1, len_2):
    while True:
        tmp_len = len_1
        while is_eq_double(h_1, x, h_2, p, from1, from2, tmp_len):
            len_1 = tmp_len
            if tmp_len == len_2:
                return tmp_len
            if tmp_len == (len_2 + tmp_len) // 2:
                tmp_len = (len_2 + tmp_len) // 2 + 1
            else:
                tmp_len = (len_2 + tmp_len) // 2

        if tmp_len == len_1:
            return 0
        len_2 = tmp_len - 1


def pal(h_1, x, h_2, p, ind, n):
    res = 0
    if ind != 1:
        max_len = min(ind - 1, n - ind) + 1
        tmp = bin_search_2(h_1, x, h_2, p, ind, n + 1 - ind, 2, max_len)
        res += tmp - 1 if tmp != 0 else 0
    max_len = min(ind, n - ind) + 1
    tmp = bin_search_2(h_1, x, h_2, p, ind, n - ind, 2, max_len)
    res += tmp - 1 if tmp != 0 else 0
    return res


def main():
    s = input()
    n = len(s)
    p = 10**9 + 7
    x_ = 257
    h_1 = [0] * (n + 1)
    x = [0] * (n + 1)
    x[0] = 1
    h_2 = [0] * (n + 1)
    s = ' ' + s

    for i in range(1, n + 1):
        h_1[i] = (h_1[i - 1] * x_ + ord(s[i])) % p
        x[i] = (x[i - 1] * x_) % p

        h_2[i] = (h_2[i - 1] * x_ + ord(s[n + 1 - i])) % p


    res = n

    for i in range(1, n):
        res += pal(h_1, x, h_2, p, i, n)

    print(res)


if __name__ == '__main__':
    main()