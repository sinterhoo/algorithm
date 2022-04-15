
# 문제링크 : https://www.acmicpc.net/problem/1914


def solved(n, start, ends, mid):
    if n == 1:
        print(start, ends)
        return
    solved(n-1, start, mid, ends)
    print(start, ends)
    solved(n-1, mid, ends, start)



n = int(input())

print(2**n -1)

if n <= 20:
    solved(n, 1, 3, 2)