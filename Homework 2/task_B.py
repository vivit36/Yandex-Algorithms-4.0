def is_eq(h, x, p, from1, from2, slen):
    return (
        (h[from1 + slen - 1] + h[from2 - 1] * x[slen]) % p ==
        (h[from2 + slen - 1] + h[from1 - 1] * x[slen]) % p
    )


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

    res = n

    for i in range(1, n):
        if is_eq(h, x, p, 1, n - i + 1, i):
            res = n - i

    print(res)


if __name__ == '__main__':
    main()