import sys
from collections import defaultdict

n = int(input())

dicts = defaultdict(int)

# 최빈값 list 횟수, 키
values = [[0,0]]

numbers = []

for i in range(n):
    temp = int(sys.stdin.readline())
    dicts[temp] += 1
    if values[0][0] < dicts[temp]:
        values = [[dicts[temp],temp]]
    elif values[0][0] == dicts[temp]:
        values.append([dicts[temp],temp])
    numbers.append(temp)

numbers.sort()

mode_value = 0
min_value = min(numbers)
max_value = max(numbers)
values.sort(key= lambda x : x[1])

if len(values) > 1:
    mode_value = values[1][1]
else:
    mode_value = values[0][1]

print(round(sum(numbers)/n))
print(numbers[n//2])
print(mode_value)
print(abs(min_value-max_value))




