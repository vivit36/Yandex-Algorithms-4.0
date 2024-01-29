def isvalid(s):
    stack = list()
    for elem in s:
        match elem:
            case '(' | '[' | '{':
                stack.append(elem)
            case ')':
                if not stack:
                    return 'no'
                if stack.pop() != '(':
                    return 'no'
            case ']':
                if not stack:
                    return 'no'
                if stack.pop() != '[':
                    return 'no'
            case '}':
                if not stack:
                    return 'no'
                if stack.pop() != '{':
                    return 'no'
    if len(stack) != 0:
        return 'no'
    else:
        return 'yes'


def main():
    str = input()
    print(isvalid(str))


if __name__ == '__main__':
    main()