from itertools import combinations



li =[9,8,7,6,5,4,3,2,1,0]
x = int(input())
nums = set()
for i in range(1, 11):
    temp = list(combinations(li, i))
    temp.sort(reverse=True)
    for k in temp:
        nums.add(int(''.join(map(str,k))))
nums = list(nums)
nums.sort()

try:
    print(nums[x])
except:
    print(-1)