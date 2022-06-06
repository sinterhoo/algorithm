
from types import TracebackType


def largestNumber(nums) -> str:
    new_nums = []
    for i in range(len(nums)):
        new_nums.append(str(nums[i]))
    new_nums.sort(key = lambda x : int(x[0]))
    temp = ''
    for i in nums:
        temp += str(i)
    return temp



print(largestNumber([10,2]))
        