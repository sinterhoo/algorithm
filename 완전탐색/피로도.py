from itertools import permutations

def solution(k, dungeons):
    answer = 0
    nums = [i for i in range(len(dungeons))]
    
    nums = list(permutations(nums,len(dungeons)))
    
    for num_list in nums:
        temp = k
        temp_answer = 0
        for idx in num_list:
            if dungeons[idx][0] <= temp:
                temp_answer += 1
                temp -= dungeons[idx][1]
        answer = max(answer, temp_answer)
    
    return answer