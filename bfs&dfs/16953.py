# 지수승은 2의 30승이면 10억
# 1을 붙이는건 자릿수가 올라감
# 재귀로 하더라도 충분해 보임

a,b = map(int, input().split())

check = 0
answer = 1e9
def solved(n,count):
    global check
    global answer
    if n > b:
        return
    if n == b:
        check = 1
        answer = min(answer, count+1)
        return
    solved(n*2,count+1)
    temp = ''
    temp = str(n)+'1'
    solved(int(temp), count+1)
    return

solved(a,0)
if check == 1:
    print(answer)
else:
    print(-1)