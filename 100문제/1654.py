import sys


K,N = map(int, input().split())
lan_list = []

for _ in range(K):
    lan_list.append(int(sys.stdin.readline()))
sum_lan = sum(lan_list)

lan_list.sort()

start = 1

end = lan_list[-1]

answer = 0

while start <= end:
    mid = (start + end)//2
    temp_sum = 0
    if sum_lan < mid:
        end = mid -1
        continue
    for i in lan_list:
        temp_sum += i//mid
    
    if temp_sum >= N:
        answer = max(answer, mid)
        start = mid +1
    else:
        end = mid -1


print(answer)