from collections import Counter
from itertools import combinations


n,k = map(int, input().split())
alphabet_list = []
str_list = []
answer = 0

count_list = []

for _ in range(n):
    str_list.append(input())

if k < 5:
    print(0)
else:
    for b in str_list:
        temp = Counter(b)
        count_list.append(temp)
        for key,value in temp.items():
            if not key in alphabet_list:
                alphabet_list.append(key)

    com_list = list(combinations(alphabet_list, k))


    for z in com_list:
        answer_temp = 0
        for i in count_list:
            if len(i) <= k:
                for key,value in i.items():
                    if not key in z:
                        break
                else:
                    answer_temp +=1
        else:
            answer = max(answer, answer_temp)

    print(answer)