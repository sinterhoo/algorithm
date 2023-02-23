# import sys

# t = int(input())

# for _ in range(t):
#     k = int(input())
#     nums = []
#     for _ in range(k):
#         order = sys.stdin.readline().split()
#         if order[0] == 'I':
#             nums.append(int(order[1]))
#         else:
#             nums.sort()
#             if order[1] == '-1':
#                 if len(nums) != 0:
#                     nums.pop(0)
#             else:
#                 if len(nums) != 0:
#                     nums.pop()
#     else:
#         nums.sort()
#         if len(nums) == 0:
#             print('EMPTY')
#         elif len(nums) == 0:
#             print(nums[0],nums[0])
#         else:
#             print(nums[-1],nums[0])


import sys
import heapq

t = int(input())

for _ in range(t):
    k = int(input())
    min_heap = []
    max_heap = []
    count = 0
    for _ in range(k):
        order = sys.stdin.readline().split()
        if order[0] == 'I':
            heapq.heappush(min_heap, int(order[1]))
            heapq.heappush(max_heap, -int(order[1]))
            count += 1
        else:
            if count == 0:
                continue
            count -= 1
            if order[1] == '-1':
                heapq.heappop(min_heap)
                max_heap = [-x for x in min_heap]
                heapq.heapify(max_heap)
            else:
                heapq.heappop(max_heap)
                min_heap = [-x for x in max_heap]
                heapq.heapify(min_heap)
    else:
        if count == 0:
            print('EMPTY')
        elif count == 1:
            print(min_heap[0], min_heap[0])
        else:
            print(-max_heap[0],min_heap[0])