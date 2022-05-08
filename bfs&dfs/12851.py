from collections import deque


n,k = map(int, input().split())


def solved(n, k):
    move = deque([])
    dp = [0 for _ in range(10001)]
    move.append(n)
    count = 0
    result = 0
    check = 0
    while move:
        for _ in range(len(move)):
            now = move.popleft()
            if now == k:
                result +=1
                check =1
            for i in range(3):
                if i == 0:
                    next = now -1
                elif i == 1:
                    next = now +1
                else:
                    next = now*2
                
                if 0< next <= k +(k - now)+2 and dp[next] != 1 :
                    dp[next] = 1
                    move.append(next)
        if check == 1:
            break
        count = count+1

    print(count)
    print(result)

solved(n,k)