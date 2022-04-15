import bisect

n = int(input())

number = list(map(int, input().split()))
number.sort()

m = int(input())

search_num = list(map(int, input().split()))


for i in search_num:
    is_true = bisect.bisect_left(number, i)
    if is_true >= len(number):
        print(0)
    elif number[is_true] == i:
        print(1)
    else:
        print(0)