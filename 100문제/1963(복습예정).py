from collections import deque

def is_prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, x):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

def bfs(my_num, target_num, nums):

    temp_num = [False for _ in range(10000)]
    num_list = deque()
    count = 0
    num_list.append([my_num,count])
    while num_list:
        temp = num_list.popleft()
        if temp[0] == target_num:
            return temp[1]
        temp_check_num = str(temp[0])
        temp_count = temp[1]

        for i in range(1,10):
            temp_check = int(str(i)+temp_check_num[1:])
            if nums[temp_check] and temp_num[temp_check] == False:
                temp_num[temp_check] = True
                num_list.append([temp_check, temp_count+1])
        for i in range(0,10):
            temp_check = int(temp_check_num[0]+str(i)+temp_check_num[2:])
            if nums[temp_check] and temp_num[temp_check] == False:
                temp_num[temp_check] = True
                num_list.append([temp_check, temp_count+1])
        for i in range(0,10):
            temp_check = int(temp_check_num[0:2]+str(i)+temp_check_num[3])
            if nums[temp_check] and temp_num[temp_check] == False:
                temp_num[temp_check] = True
                num_list.append([temp_check, temp_count+1])
        for i in range(0,10):
            temp_check = int(temp_check_num[:3]+str(i))
            if nums[temp_check] and temp_num[temp_check] == False:
                temp_num[temp_check] = True
                num_list.append([temp_check, temp_count+1])
    return -1
T = int(input())

nums = [False for _ in range(10000)]

for i in range(10000):
    nums[i] = is_prime_number(i)


for i in range(T):
    my_num, target_num = map(int, input().split())

    answer = bfs(my_num,target_num,nums)
    if answer == -1:
        print("Impossible")
    else:
        print(answer)


