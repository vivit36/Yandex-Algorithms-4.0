def skobki(n, skob_lst, visited, cnt=0, res=[], stack=[], lvl=0):
    if len(res) == n and len(stack) == 0:
        print(''.join(map(str, res)))
    elif len(res) != n:
        for i in range(len(skob_lst)):
            if visited[lvl][i] is False:
                if len(stack) >= n // 2 + 1 or cnt > n - lvl:
                    return
                elif skob_lst[i] == ')':
                    if len(stack) == 0:
                        continue
                    else:
                        if stack[-1] != '(':
                            continue
                        else:
                            tmp = stack.pop()
                            visited[lvl][i] = True
                            res.append(skob_lst[i])
                            cnt -= 1
                            skobki(n, skob_lst, visited, cnt, res, stack, lvl + 1)
                            visited[lvl][i] = False
                            cnt += 1
                            res.pop()
                            stack.append(tmp)
                elif skob_lst[i] == ']':
                    if len(stack) == 0:
                        continue
                    else:
                        if stack[-1] != '[':
                            continue
                        else:
                            tmp = stack.pop()
                            visited[lvl][i] = True
                            res.append(skob_lst[i])
                            cnt -= 1
                            skobki(n, skob_lst, visited, cnt, res, stack, lvl + 1)
                            visited[lvl][i] = False
                            cnt += 1
                            res.pop()
                            stack.append(tmp)
                else:
                    visited[lvl][i] = True
                    res.append(skob_lst[i])
                    stack.append(skob_lst[i])
                    cnt += 1
                    skobki(n, skob_lst, visited, cnt, res, stack, lvl + 1)
                    stack.pop()
                    cnt -= 1
                    visited[lvl][i] = False
                    res.pop()


def main():
    n = int(input().strip())
    skob_lst = ['(', '[', ')', ']']
    visited = [[False] * 4 for _ in range(n)]

    skobki(n, skob_lst, visited)


if __name__ == '__main__':
    main()
