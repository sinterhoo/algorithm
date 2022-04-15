

# 먼저 같은 열에는 퀸을 놓지 않는다는 가정을 하고 각 열의 i 번째에 퀸을 놓는다는 것을 표시하기 위한 1차원 리스트를 만든다.
# 여기서 편의상 1번 인덱스 ~ n번 인덱스까지 1열 ~ n열을 표시하기 위해 n+1 만큼의 리스트를 초기화하고 0번쨰 인덱스에는 정답을 넣는다.
# solved 함수는 재귀함수이며 i열의 j 번째 행에 퀸을 놓는다. 여기서 check 함수를 통과하지 못하면 백트래킹을 해준다.

# check 함수는 간단하다. 내가 재귀함수를 통해 i열 j번째 행에 퀸을 놓았을 때 그 위치가 유효한지 체크해주는 함수이다.
# 같은 열에는 놓지 않는다는 것은 전제 조건이므로 체크해야 할 것은

# 1. 같은 행인지 col[i] == col[k] 로 검증을 하고
# 2. 같은 대각선인지 abs(col[i] - col[k]) == (i- k) 로 검증을 해준다.
# 이 때 한가지라도 걸리게 된다면 false를 호출하고 그 뒤의 경우의 수는 고려할 필요가 없으므로 백트래킹 해준다.

def check(i, col):
    k = 1
    flag = True
    while(k < i and flag):
        if (col[i] == col[k]) or (abs(col[i] - col[k]) == (i - k)):
            flag = False
        k = k+1
    return flag




def solved(i, col, result):
    n = len(col)-1

    if check(i, col):
        if i == n:
            result[0] = result[0]+1
        else:
            for j in range(1, n+1):
                col[i+1] = j
                solved(i+1, col, result)





n = int(input())

col = [0]*(n+1)
result = [0]

solved(0, col, result)
print(result[0])



# 근데 위의 코드를 제출하면 시간 초과가 난다... 개념은 알았으니 인터넷으로 시간초과를 해결해 보았다.

# 시간 초과가 나는 이유 = 매번 재귀마다 가로, 대각선을 검증하면 너무나도 오래 걸리기에
# 미리 가로, 세로, 대각선을 저장해두고 각각 계산을 해야 통과가 가능하다.

# 참고 링크 : https://rebas.kr/761

""" n, ans = int(input()), 0
a, b, c = [False]*n, [False]*(2*n-1), [False]*(2*n-1)

def solve(i):
    global ans
    if i == n:
        ans += 1
        return
    for j in range(n):
        if not (a[j] or b[i+j] or c[i-j+n-1]):
            a[j] = b[i+j] = c[i-j+n-1] = True
            solve(i+1)
            a[j] = b[i+j] = c[i-j+n-1] = False

solve(0)
print(ans) """