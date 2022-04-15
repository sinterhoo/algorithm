# 메모리가 매우 작기 때문에 모든 입력값을 저장해서는 메모리 초과가 나옴
# 그래서 정해둔 리스트를 만들고 1번째 인덱스에는 1 숫자의 입력 개수를 저장하는 식으로 하고
# 해당 리스트를 활용해 출력을 진행함


import sys

N = int(input())

result = [0] * 10001
for i in range(N):
    x = int(sys.stdin.readline())
    result[x] = result[x] + 1

for k in range(1, 10001):
    while result[k] > 0:
        print(k)
        result[k] = result[k] - 1