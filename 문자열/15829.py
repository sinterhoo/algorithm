al = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

n = int(input())
s = input()
answer = 0
count = 0
for i in s:
    index = al.index(i)
    temp = (index+1) * (31**count)
    answer += (temp)
    count +=1

print(int(answer%1234567891))