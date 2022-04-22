# 10만의 입력값이므로 시간복잡도 O(nlogn) 을 생각해야 했음
# 너무 복잡하게 생각해서 시간초과가 많이 났는데, 면접 결과를 기준으로 오름차순 정렬하고
# 기준이 되는 서류심사 성적을 첫 사원의 값으로 하고 그 뒤로 for문을 돌며 min 값으로 바꿔치기 하면서 비교하면
# nlogn + n 의 시간 복잡도를 가지게 된다.


import sys

t = int(input())

for _ in range(t):
    n = int(input())
    person = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
  
    person.sort(key = lambda x: x[0])

    mins = person[0][1]
    for i in range(1, len(person)):
        if mins < person[i][1]:
            n-=1
        else:
            mins = person[i][1]
    print(n)
