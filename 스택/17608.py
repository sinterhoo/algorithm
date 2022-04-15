import sys

n = int(input())

num_list = [int(sys.stdin.readline().strip()) for _ in range(n)]

max = num_list[len(num_list)-1]
count = 1
for i in range(n):
    temp = num_list.pop()
    if temp > max:
        count = count+1
        max = temp

print(count)