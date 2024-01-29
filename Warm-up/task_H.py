def count_contest(a, b, n):
    kr = a // n if a % n == 0 else a // n + 1
    kl = a

    mr = b // n if b % n == 0 else b // n + 1
    ml = b

    if kr > kl or mr > ml:
        return 'No'

    if kl > mr:
        return 'Yes'
    else:
        return 'No'


def main():
    a = int(input())
    b = int(input())
    n = int(input())

    print(count_contest(a, b, n))


if __name__ == '__main__':
    main()