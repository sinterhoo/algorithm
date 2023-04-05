import heapq

def solution(n, works):
    answer = 0
    heap_list = []
    for i in works:
        heapq.heappush(heap_list,-i)
    
    while n != 0:
        temp = heapq.heappop(heap_list)
        temp += 1
        heapq.heappush(heap_list,temp)
        n -= 1
    for i in heap_list:
        if i < 0:
            i = i * -1
            answer += i**2
    return answer