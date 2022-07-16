import sys


N = int(input())

nums = list(map(int, sys.stdin.readline().split()))

limit_num = int(input())

nums.sort()
left = 0
right = nums[-1]
sum_check = sum(nums)

if sum_check <= limit_num:
    print(right)
else:
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        temp = 0
        for i in nums:
            if i > mid:
                temp += mid
            else:
                temp += i
        if temp > limit_num:
            right = mid -1
        else:
            answer= max(answer, mid)
            left = mid+1

    print(answer)