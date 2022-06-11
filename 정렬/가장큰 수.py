
lists = [3, 30, 34, 5, 9]

lists = list(map(str,lists))

lists.sort(key = lambda x:x*3, reverse=True)

print(lists)