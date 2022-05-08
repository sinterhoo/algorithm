height = [4,2,0,3,2,5]


mid = [0,0]
start = [0,0]
end = [0,0]
for i in range(len(height)):
    if start[0] == 0 and height[i] != 0:
        start = [height[i], i]
    if mid[0] < height[i]:
        mid = [height[i], i]

for i in range(len(height)-1, -1, -1):
    if height[i] != 0:
        end = [height[i], i]
        break
result = 0

# 시작부터 끝

for i in range(start[1]+1, mid[1]+1):
    if start[0] <= height[i]:
        result += (i-start[1]-1) * start[0]
        for j in range(start[1]+1, i):
            result -= height[j]
        start = [height[i], i]

for i in range(end[1]-1, mid[1]-1, -1):
    if end[0] <= height[i]:
        result += (end[1]-i -1) * end[0]
        for j in range(end[1]-1, i, -1):
            result -= height[j]
        end = [height[i], i]

print(result)