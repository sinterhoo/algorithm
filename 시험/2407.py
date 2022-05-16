

n,m = map(int, input().split())
temp = 1
temp2 = 1
for i in range(n, n-m, -1):
    temp *= i
for j in range(m, 0, -1):
    temp2 *= j

print(temp//temp2)