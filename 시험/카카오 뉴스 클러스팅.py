from collections import defaultdict
import math

def solution(str1, str2):
    answer = 0
    temp_str1 = []
    temp_str2 = []
    
    str1_dict = defaultdict(int)
    str2_dict = defaultdict(int)
    
    all_list = 0
    same_list = 0
    for i in range(len(str1)):
        if i == len(str1)-1:
            break
        temp = str1[i:i+2]
        if temp.isalpha():
            temp = temp.upper()
            temp_str1.append(temp)
            str1_dict[temp] +=1
    for i in range(len(str2)):
        if i == len(str2)-1:
            break
        temp = str2[i:i+2]
        if temp.isalpha():
            temp = temp.upper()
            temp_str2.append(temp)
            str2_dict[temp] +=1
    
    for key, value in str1_dict.items():
        if str2_dict[key] < 1:
            all_list +=value
        elif str2_dict[key] >= value:
            all_list += str2_dict[key]
            same_list +=value
    
    for key, value in str2_dict.items():
        if value > 0:
            if str1_dict[key] < 1:
                all_list +=value
            elif str1_dict[key] > value:
                all_list += str1_dict[key]
                same_list +=value
    if all_list == 0:
        return 65536
    answer = math.trunc((same_list / all_list) * 65536)
    
    return answer


print(solution('FRANCE','french'))