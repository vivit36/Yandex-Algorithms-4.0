def perestanovki(n, visited, res=[]):
    if len(res) == n:
        print(''.join(map(str, res)))
    else:
        for i in range(1, n + 1):
            if visited[i] is False:
                visited[i] = True
                res.append(i)
                perestanovki(n, visited, res)
                visited[i] = False
                res.pop()


def main():
    n = int(input().strip())
    visited = [False] * (n + 1)
    perestanovki(n, visited)


if __name__ == '__main__':
    main()
