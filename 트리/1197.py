import sys


def find_parents(parent, a):
    if parent[a] != a:
        parent[a] = find_parents(parent, parent[a])
    return parent[a]

def union_parents(parent, a, b):
    a = find_parents(parent, a)
    b = find_parents(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

V,E = map(int, input().split())


parents = [i for i in range(V+1)]

list1 = []
result = 0

for i in range(E):
    x1,x2,cost = map(int, sys.stdin.readline().split())
    list1.append([cost,x1,x2])

list1.sort()


for i in list1:
    cost,x1,x2 = i

    if find_parents(parents, x1) != find_parents(parents, x2):
        union_parents(parents, x1, x2)
        result = result + cost

print(result)