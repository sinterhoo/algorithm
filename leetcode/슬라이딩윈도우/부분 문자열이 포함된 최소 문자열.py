from collections import Counter
from collections import defaultdict

def minWindow(s: str, t: str) -> str:
        t_list = Counter(t)
        start_index = 0
        end_index = 1
        
        answer_max = [0,len(s)+1]
        if len(s) == 1:
            if s != t:
                return ""
            else:
                return t
        temp = defaultdict(int)
        temp[s[start_index]] +=1
        while end_index <= len(s):
            for key, value in t_list.items():
                if temp[key] < value:
                    end_index +=1
                    temp[s[end_index-1]] +=1
                    break
            else:
                if answer_max[1] - answer_max[0] >= end_index - start_index:
                    answer_max = [start_index, end_index]
                start_index +=1
                temp[s[start_index-1]] -= 1
        if answer_max[0] == 0 and answer_max[1] == len(s)+1:
            return ""
        return s[answer_max[0]:answer_max[1]]

print(minWindow("ADOBECODEBANC", "ABC"))