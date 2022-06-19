import sys
from collections import Counter

s = sys.stdin.readline().rstrip()

s_dict = Counter(s)

al = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in al:
    print(s_dict[i],end=' ')
