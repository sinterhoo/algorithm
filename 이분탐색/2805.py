from sys import stdin
import bisect

n, m = map(int, input().split())

trees = list(map(int, stdin.readline().split()))
trees.sort()

end_num = trees[len(trees)-1]
start_num = 0
result = 0

while start_num <= end_num:
    mid_num = (end_num+start_num)//2
    check_num = bisect.bisect_left(trees, mid_num)
    answer = sum(trees[check_num:]) - mid_num*len(trees[check_num:])

    if answer >= m:
        start_num = mid_num+1
        result = mid_num
    else:
        end_num = mid_num-1

print(result)


# 복습 코드

""" 
import sys

n,m = map(int, input().split())

tree = list(map(int, sys.stdin.readline().split()))
tree.sort()

left = 0
right = tree[n-1]
result = 0
while left <= right:
    mid = (left+right)//2
    sum_tree = 0
    for i in tree:
        if i > mid:
            sum_tree = sum_tree + i - mid
    if sum_tree >= m:
        result = max(result, mid)
        left = mid+1
    else:
        right = mid-1

print(result) """