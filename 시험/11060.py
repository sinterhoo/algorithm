import sys
from collections import deque

n = int(input())

nums = list(map(int, sys.stdin.readline().split()))
dp = [-1 for _ in range(len(nums)+1)]
move = deque()

move.append([nums[0],0,0])

while move:
    for _ in range(len(move)):
        temps,index,count = move.popleft()
        if dp[index] == -1:
            dp[index] = count
        i = temps
        while i != 0:
            if index+i < len(nums):
                if dp[index+i] == -1:
                    move.append([nums[index+i],index+i,count+1])
            i -=1


print(dp[len(nums)-1])