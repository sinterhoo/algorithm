


n,w = map(int, input().split())

while n != 0 and w != 0:
    temp = []
    for _ in range(n):
        temp.append(int(input()))

    temp.sort()
    stick = [0 for _ in range(100//w + 1)]

    for i in temp:
        stick[i//w] += 1
    
    last_index = 0
    color_count = 0
    max_color = 0
    for k in range(len(stick)):
        if stick[k] != 0:
            if max_color < stick[k]:
                max_color = stick[k]
            last_index = k
            color_count += 1
    now_count = last_index
    color_count = last_index
    color = 1
    answer = 0
    for k in range(len(stick)):
        color = now_count / color_count
        if stick[k] != 0:
            answer += (color*(stick[k]/max_color))
        now_count -=1
    answer = answer + 0.01
    print(answer)

    n,w = map(int, input().split())
