
n,m = map(int, input().split())

a = set(map(int, input().split()))
b = set(map(int, input().split()))


s1 = a-b
s2 = b-a

print(len(s1)+len(s2))