def is_eq(h, x, p, from1, from2, slen):
    return (
        (h[from1 + slen - 1] + h[from2 - 1] * x[slen]) % p ==
        (h[from2 + slen - 1] + h[from1 - 1] * x[slen]) % p
    )


def bin_search(h, x, p, from1, from2, len_1, len_2):
    tmp_len = len_1
    while is_eq(h, x, p, from1, from2, tmp_len):
        len_1 = tmp_len
        if tmp_len == len_2:
            return tmp_len
        if tmp_len == (len_2 + tmp_len) // 2:
            tmp_len = (len_2 + tmp_len) // 2 + 1
        else:
            tmp_len = (len_2 + tmp_len) // 2

    if tmp_len == len_1:
        return 0

    return bin_search(h, x, p, from1, from2, len_1, tmp_len - 1)


def main():
    s = input()
    n = len(s)
    p = 10**9 + 7
    x_ = 257
    h = [0] * (n + 1)
    x = [0] * (n + 1)
    x[0] = 1
    s = ' ' + s
    for i in range(1, n + 1):
        h[i] = (h[i - 1] * x_ + ord(s[i])) % p
        x[i] = (x[i - 1] * x_) % p

    res = [0] * n

    for i in range(2, n + 1):
        res[i - 1] = bin_search(h, x, p, 1, i, 1, n + 1 - i)

    print(' '.join(map(str, res)))


if __name__ == '__main__':
    main()