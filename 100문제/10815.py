import sys


N = int(input())

my_card_list = list(map(int, sys.stdin.readline().split()))
my_card_list.sort()

M = int(input())

check_card_list = list(map(int, sys.stdin.readline().split()))

for i in check_card_list:
    left = 0
    right = N-1
    while left <= right:
        mid = (left + right)//2

        if my_card_list[mid] == i:
            print("1",end = ' ')
            break
        elif my_card_list[mid] < i:
            left = mid+1
        else:
            right = mid-1
    else:
        print("0", end = ' ')
