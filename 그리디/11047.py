# 접근 방법 -> 그냥 지문에서의 요구 사항대로 구현

import sys

n,k = map(int, input().split())

coin =[]
for _ in range(n):
    temp = int(sys.stdin.readline())

    coin.append(temp)

coin.sort(reverse=True)

count = 0
number = 0
while k > 0:
    if k - coin[number] >= 0:
        k = k - coin[number]
        count +=1
    else:
        number+=1

print(count)