# 접근 방식 -> 회의가 끝나는 시간, 시작하는 시간 순으로 정렬을 하고
# 0번째 인덱스부터 탐욕적으로 탐색하면 정답이 나온다.

import sys

n = int(input())

nums = []

for _ in range(n):
    start,end = map(int, sys.stdin.readline().split())

    nums.append([start,end])

nums.sort(key = lambda x : (x[1],x[0]))

start = nums[0][0]
end = nums[0][1]
count = 1
for i in range(1, len(nums)):
    if end <= nums[i][0]:
        start = nums[i][0]
        end = nums[i][1]
        count +=1

print(count)
    