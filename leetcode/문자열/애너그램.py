strs = ["eat","tea","tan","ate","nat","bat"]
strs.sort()

check = []
answer = []

for i in strs:
    temp = list(i)
    temp.sort()
    temp = ''.join(temp)

    for j in range(len(answer)):
        if answer[j][0] == temp:
            answer[j].append(i)
            break
    else:
        answer.append([temp])
        answer[-1].append(i)


for i in range(len(answer)):
    answer[i] = answer[i][1:]

answer.sort()

