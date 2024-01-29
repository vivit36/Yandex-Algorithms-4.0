from collections import Counter


def anagram(str1, str2):
    if Counter(str1) == Counter(str2):
        return "YES"
    else:
        return "NO"


def main():
    str1 = input()
    str2 = input()
    print(anagram(str1, str2))


if __name__ == '__main__':
    main()