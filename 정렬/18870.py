import sys

n = int(input())

nums = list(map(int, sys.stdin.readline().split()))
sort_nums = sorted(list(set(nums)))
dict_nums = {}
start_count = 0
for number in sort_nums:
    dict_nums[number] = start_count
    start_count +=1

for i in range(n):
    nums[i] = dict_nums[nums[i]]

print(*nums)