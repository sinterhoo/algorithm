import sys


n = int(input())

s = sys.stdin.readline().rstrip()

answer = 0
start_index = -1
for i in range(len(s)):
    if s[i].isdigit() and start_index == -1:
        start_index = i
    if s[i].isalpha() and start_index != -1:
        answer += int(s[start_index:i])
        start_index = -1

if start_index != -1:
    answer += int(s[start_index:])

print(answer)