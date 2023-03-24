## set과 dict의 시간복잡도 차이
## 123, 12345 와 12345, 123 둘다 일관성이 없다. 정렬을 해주어서 길이를 고려해주었다.


# import sys
# t = int(sys.stdin.readline())

# for i in range(t):
#     n = int(sys.stdin.readline())
#     substrings = set()
#     answer = 'YES'
#     str_list = []
#     for k in range(n):
#         str1 = sys.stdin.readline().rstrip()
#         str_list.append(str1)
#     str_list.sort()
#     for str1 in str_list:
#         temp_str = ''
#         for s in str1:
#             temp_str += s
#             if temp_str in substrings:
#                 answer = 'NO'
#                 break
#         else:
#             substrings.add(str1)
#             continue
#         break
#     print(answer)

import sys
t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    substrings = dict()
    answer = 'YES'
    str_list = []
    for k in range(n):
        str1 = sys.stdin.readline().rstrip()
        str_list.append(str1)
    str_list.sort()
    for str1 in str_list:
        temp_str = ''
        for s in str1:
            temp_str += s
            if temp_str in substrings:
                answer = 'NO'
                break
        else:
            substrings[str1] = 1
            continue
        break
    print(answer)