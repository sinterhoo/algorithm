from collections import deque

def search(nums, target) -> int:
    count =0
    start = 0
    end = len(nums)-1
    
    while start <= end:
        mid = (start + end)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            end = mid-1
        else:
            start = mid+1
    else:
        return -1
     

print(search([4,5,6,7,0,1,2], 0))