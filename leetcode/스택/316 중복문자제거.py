from collections import defaultdict
from string import ascii_lowercase


def removeDuplicateLetters(s: str) -> str:
    
    als = defaultdict(list)
    alpha = list(ascii_lowercase)
    
    for i in range(len(s)):
        als[s[i]].append(i)
        
    
    print(als)                    
    return s

s = removeDuplicateLetters("cbacdcbc")