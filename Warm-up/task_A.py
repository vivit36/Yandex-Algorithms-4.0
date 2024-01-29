def not_minimum(sequence, request):
    first_item = sequence[request[0]]
    for i in range(request[0], request[1] + 1, 1):
        if sequence[i] != first_item:
            return str(max(sequence[i], first_item))
    return "NOT FOUND"


def main():
    input_str = input().split(' ')
    n, m = int(input_str[0]), int(input_str[1])
    lst = [int(x) for x in input().split(' ')]
    result = list()
    for i in range(m):
        req = [int(x) for x in input().split(' ')]
        result.append(not_minimum(lst, req))

    print('\n'.join(result))


if __name__ == '__main__':
    main()