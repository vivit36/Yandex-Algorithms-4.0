def elevator(k, n, people):
    res = 0
    buf = 0
    last_flor = n
    for i in range(n, 0, -1):
        tmp = people.pop()
        if buf != 0:
            if tmp != 0:
                if tmp >= k - buf:
                    tmp = tmp - (k - buf)
                    buf = 0
                    res += last_flor * 2
                    # cod nizhe
                else:
                    buf += tmp
                    continue
            else:
                continue


        c_part = tmp // k
        res += c_part * 2 * i
        buf = tmp % k
        last_flor = i

    if buf != 0:
        res += last_flor * 2

    return res


def main():
    k = int(input())
    n = int(input())
    people = list()
    for i in range(n):
        people.append(int(input()))

    print(elevator(k, n, people))


if __name__ == '__main__':
    main()