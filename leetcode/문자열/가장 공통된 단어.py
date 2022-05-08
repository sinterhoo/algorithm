from collections import defaultdict

paragraph = "Bob. hIt, baLl"
banned =["bob", "hit"]
dicts = defaultdict(int)

str_list = []
temp = ''
for i in paragraph:
    if i.isalpha():
        temp += i
    else:
        if temp != '':
            str_list.append(temp)
            temp = ''
if len(temp) != 0:
    str_list.append(temp)

for i in str_list:
    i = i.lower()
    dicts[i] += 1
maxs = []
for key, value in dicts.items():
    if key in banned:
        continue
    if len(maxs) == 0:
        maxs = [key, value]
        continue
    if maxs[1] < value:
        maxs = [key, value]
        continue

print(maxs[0])