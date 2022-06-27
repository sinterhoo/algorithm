def solution(m, musicinfos):
    answer = ''
    answer_list = []
    for i in musicinfos:
        temp = i.split(',')
        time1 = int(temp[1][:2]) - int(temp[0][:2])
        time2 = int(temp[1][3:]) - int(temp[0][3:])
        name = temp[2]
        temp_list = [time1,time2,name]
        
        music_temp1 = ''
        
        while len(music_temp1)< len(m):
            music_temp1 += temp[3]
        
        music_temp = max(temp[3]+temp[3]+temp[3],music_temp1)
        
        for j in range(len(music_temp)):
            start = j
            check = 0
            for k in range(len(m)):
                if start >= len(music_temp):
                    break
                if m[k] != music_temp[start]:
                    break
                start +=1
            else:
                if start < len(music_temp):
                    if music_temp[start] == '#':
                        check = 0
                    else:
                        check = 1
                        break
                else:
                    check = 1
                    break
            if check == 1:
                answer_list.append(temp_list)
                break
                
    
    answer_list.sort(reverse=True)
    print(answer_list)
    return answer_list[0][2]


print(solution("ABC",["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))