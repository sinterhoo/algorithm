

# 문제 링크 : https://www.acmicpc.net/problem/5568

# 재귀로 풀지 않고 반복문을 이용 (재귀로 풀 수 있는 문제는 반복문으로 풀 수 있고 반복문으로 풀 수 있는 문제는 재귀로 풀 수 있기에..)
# 각 경우의 수(순열)를 list2에 저장하고 list2에 ('1','2','3') 이런식으로 저장된 요소들을 ('123') 으로 변경하여 list3에 저장
# list3에 set을 이용하여 중복을 제거해 완성

from itertools import permutations

n = int(input())
k = int(input())

list1 = []

for i in range(n):
    x = input()
    list1.append(x)


list2 = list(permutations(list1, k))
list3 =[]
for i in range(len(list2)):
    str1 = ''
    for j in range(len(list2[i])):
        str1 = str1 + list2[i][j]
    list3.append(str1)


my_set = set(list3)
my_list = list(my_set)

print(len(my_list))
