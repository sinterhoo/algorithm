from collections import deque


S = int(input())

visited = [[-1 for _ in range(1001)] for _ in range(1001)]

emoticon = deque()

# 이모티콘 수, 클립보드, 시간
emoticon.append([1,0,0])

while emoticon:
    temp_emo = emoticon.popleft()
    temp_clip = temp_emo[1]
    temp_time = temp_emo[2]
    temp_emo = temp_emo[0]

    if temp_emo < 1:
        continue
    if temp_emo > S:
        continue

    if visited[temp_emo][temp_emo] == -1:
        emoticon.append([temp_emo, temp_emo, temp_time+1])
        visited[temp_emo][temp_emo] = temp_time+1
    if temp_emo+temp_clip <= S and visited[temp_emo+temp_clip][temp_clip] == -1:
        emoticon.append([temp_emo+temp_clip, temp_clip, temp_time+1])
        visited[temp_emo+temp_clip][temp_clip] = temp_time+1
    if temp_emo-1 > 1 and visited[temp_emo-1][temp_clip] == -1:
        emoticon.append([temp_emo-1,temp_clip,temp_time+1])
        visited[temp_emo-1][temp_clip] = temp_time+1

answer = 1000000
for i in range(0,1001):
    if visited[S][i] != -1:
        answer = min(answer, visited[S][i])
print(answer)