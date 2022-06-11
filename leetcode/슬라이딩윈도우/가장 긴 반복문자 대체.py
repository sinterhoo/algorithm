from collections import defaultdict


def characterReplacement(s: str, k: int) -> int:
        start = 0
        end = 1
        
        if len(s) == 1:
            return s
        
        temp = k
        max_len = -1
        answer = 0
        
        str_dict = defaultdict(int)
        str_dict[s[start]] +=1
        str_dict[s[end]] +=1
        
        while end < len(s):
            temp_num = 0
            max_str = 0
            for key,values in str_dict.items():
                if max_str < values:
                    temp_num += max_str
                    max_str = values
                else:
                    temp_num += values
            
            if temp_num > k:
                start +=1
                if start > len(s)-1:
                    break
                str_dict[s[start]] -=1
            else:
                answer = max(answer, end-start+1)
                end +=1
                if end > len(s)-1:
                    break
                str_dict[s[end]] +=1
            
            
        return answer

print(characterReplacement("ABAA",0))