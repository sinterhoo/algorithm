class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        start = 0
        
        answer= ''
        while True:
            end = len(s)
            if start == end:
                break
            if len(answer) > len(s[start:]):
                break
            while True:
                if start == end:
                    if len(s[start]) > len(answer):
                        answer = s[start]
                    break
                start_temp = ''
                end_temp =''
                start_temp = s[start:end]
                end_temp = start_temp[::-1]
                
                if start_temp == end_temp:
                    if len(answer) < len(start_temp):
                        answer = start_temp
                        break
                end -= 1
            start += 1
                
        return answer