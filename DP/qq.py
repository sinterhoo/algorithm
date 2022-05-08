import sys

n = int(sys.stdin.readline())
roads = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))
dp = list([0] * (1 << n - 1) for _ in range(n))


# all_visited = (1 << n - 1) - 1 # 더 오래걸림.
# inf = 1e9  # sys.maxsize 보단 빠른데 하나하나 1e9 써주는게 더빠름.


def get_tsp(now, route):
    if dp[now][route]:  # (0이 아니라면), 현재 온 곳의 route 가 이미 기록된 경로 라면,
        return dp[now][route]  # 저장된 값을 리턴해라! (dp : memoization)
    if route == (1 << n - 1) - 1:  # 만약 모든 경로를 돌았다면, (111)
        if roads[now][0]:  # 만약 현재위치(now) 에서 출발지(0)로 가는 길이 있으면,
            return roads[now][0]  # now -> 0 으로 가는 cost 리턴해라!
        return 1e9  # 출발지로 돌아가는 길이 없으면 최대 비용을 리턴해라! (나중에 걸러주기 위해 최대값 리턴)

    bound = 1e9  # 최대 값으로 일단 초기화.
    for next in range(1, n):  # 어디서 시작하던 똑같음, 0번 도시에서 시작하고, 1번 도시부터 돈다.
        if not roads[now][next]:  # now -> next 길이없으면 패스
            continue
        if route & 1 << next - 1:  # 다음도시가 이미 들렸던 곳이면 패스.
            continue
        distance = roads[now][next] + get_tsp(next, route | (1 << next - 1))
        # 거리(비용) = 현재도시(now)에서 다음 도시(next)까지의 금액 + get_tsp(다음도시(next), 지금까지 들린경로(route) or (now << next -1))

        # -> 다음도시까지의 비용 + get_tsp(다음도시, route 에 다음도시 포함시키기(방문도장찍기))
        # bound = min(bound, distance) # 100 ms 차이
        if bound > distance:
            # 바운드 갱신
            # 예를들어, 0번도시 시작(고정)일 때.
            # for 문을 돌며, 0 > 1 > 2 > 3 > 0
            #              0 > 2 > 1 > 3 > 0
            #              0 > 3 > 1 > 2 > 0
            # bound 에 최솟값을 갱신한다.(재귀적으로, dp table에 각 for 문이 끝났을 때 bound 의 최솟값(최소비용)이 각각에 저장된다)
            bound = distance
    dp[now][route] = bound
    # get_tsp(0, 0) 을 실행하면 for 문에서 재귀적으로 최소 비용을 찾아오고, 
    # dp[now][route] 즉, dp[0][0]에 다 돌고나서 최소 비용이 저장될 것이다.
    return bound
    # return dp[0][0] 해줘도됨.


print(get_tsp(0, 0))