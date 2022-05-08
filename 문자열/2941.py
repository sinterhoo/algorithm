import sys

str_list = sys.stdin.readline().rstrip()

check = ['c=','c-','dz=','d-','lj','nj','s=','z=']
answer = 0
for i in check:
    answer += str_list.count(i)
    str_list = str_list.replace(i,'1')

str_list = str_list.replace('1','')
str_list = str_list.replace('-','')
str_list = str_list.replace('=','')

answer += len(str_list)

print(answer)