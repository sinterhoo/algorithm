
# 문제 링크 : https://www.acmicpc.net/problem/1181
# 문자열, 해당 문자열의 길이를 튜플로 리스트에 저장 후
# 튜플의 두번째 원소 (문자열의 길이)를 기준으로 정렬

n = int(input())

answer = []
for i in range(n):
    x= input()
    answer.append((x,len(x)))

my_set = set(answer)
answer = list(my_set)
answer.sort()
answer.sort(key= lambda x: x[1])

for k in answer:
    print(k[0])
