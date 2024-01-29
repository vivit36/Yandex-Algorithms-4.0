def add_fraction(a, b, c, d):
    def euclid(num1, num2):
        while num1 != 0 and num2 != 0:
            if num1 >= num2:
                num1 %= num2
            else:
                num2 %= num1
        return num1 or num2

    num1 = a * d + c * b
    num2 = b * d
    nod = euclid(num1, num2)
    return num1 // nod, num2 // nod


def main():
    a, b, c, d = map(int, input().split(' '))
    m, n = add_fraction(a, b, c, d)
    print(m, n)


if __name__ == '__main__':
    main()