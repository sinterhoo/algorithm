import sys
from collections import defaultdict



dicts = defaultdict(int)
sum_num = 0
while True:
    temp = sys.stdin.readline().rstrip()
    if not temp:
        break
    dicts[temp] +=1
    sum_num +=1

temp_list = sorted(dicts.items())
for k,v in temp_list:
    print('%s %.4f' % (k, round((v / sum_num * 100), 4)))
