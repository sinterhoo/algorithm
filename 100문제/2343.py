import sys


N,M = map(int, input().split())

num_list = list(map(int, sys.stdin.readline().split()))

num_list_sum = sum(num_list)
start = 0
end = 10000

result = 1000000

while start <= end:
    mid = (start + end)//2
    temp = 0
    count = 0
    temp_min = 1000000
    if num_list_sum > mid:
        start = mid +1
        continue

    for i in num_list:
        if temp + i > mid:
            temp_min = min(temp_min, temp)
            count +=1
            temp = 0
        if count > M:
            break
        temp += i
    
    if count <= M:
        result = min(result, temp_min)
        end = mid -1
    else:
        start = mid +1

print(result)

