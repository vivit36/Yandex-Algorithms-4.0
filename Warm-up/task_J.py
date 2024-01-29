def spread(n, a, b):
    if n % a <= n // a * (b - a):
        return 'YES'
    else:
        return 'NO'

def main():
    t = int(input())
    output_lst = list()
    for i in range(t):
        n, a, b = map(int, input().split())
        output_lst.append(spread(n, a, b))

    for el in output_lst:
        print(el)


if __name__ == '__main__':
    main()

