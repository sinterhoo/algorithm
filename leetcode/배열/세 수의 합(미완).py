from itertools import combinations


nums = [-1,0,1,2,-1,-4]
answer = []

nums = set(map(sum,combinations(nums, 3)))

nums = list(nums)


for i in nums:
    if sum(i) == 0:
        i = list(i)
        i.sort()
        if not i in answer:
            answer.append(i)


print(answer)