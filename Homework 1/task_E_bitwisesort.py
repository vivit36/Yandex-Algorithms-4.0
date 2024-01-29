def bitwisesort(i_str):
    print("Initial array:")
    print(", ".join(i_str))
    buckets = [[[] for _ in range(10)] for j in range(len(i_str[0]))]
    print("**********")
    print("Phase 1")
    digit_p = len(i_str[0]) - 1

    for str in i_str:
        tmp = int(str[digit_p])
        buckets[0][tmp].append(str)

    for i in range(10):
        print(f"Bucket {i}: ", end='')
        if len(buckets[0][i]) == 0:
            print(f"empty")
        else:
            print(", ".join(buckets[0][i]))
    print("**********")

    digit_p -= 1

    for i in range(1, len(i_str[0])):
        print(f"Phase {i+1}")
        for el in buckets[i - 1]:
            if len(el) != 0:
                for str in el:
                    tmp = int(str[digit_p])
                    buckets[i][tmp].append(str)
        digit_p -= 1
        for j in range(10):
            print(f"Bucket {j}: ", end='')
            if len(buckets[i][j]) == 0:
                print(f"empty")
            else:
                print(", ".join(buckets[i][j]))
        print("**********")

    res = list()
    for el in buckets[len(i_str[0]) - 1]:
        if len(el) != 0:
            for str in el:
                res.append(str)

    print(f"Sorted array:")
    print(", ".join(res))
    return res


def main():
    n = int(input())
    i_str = list()

    for i in range(n):
        i_str.append(input())

    bitwisesort(i_str)


if __name__ == '__main__':
    main()