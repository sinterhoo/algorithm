
# 문제 링크 : https://www.acmicpc.net/problem/10872

def solved(x):
    if x == 0:
        return 1
    else:
        return x*solved(x-1)


x = int(input())

print(solved(x))