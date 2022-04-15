# 문제 링크 : https://www.acmicpc.net/problem/10971
# 먼저 동일한 코드를 함수로 호출하지 않고 메인으로 호출하면 시간초과가 뜬다..
# 파이썬의 경우 main에 코드를 작성하면 전역변수로 취급을 하여 연산을 하게 되는데
# 전역 변수의 경우 지역 변수보다 약 2~3배 느리다!!
# 정확히 따지자면 저장하는 속도에서 매우 차이가 난다. 바이트 코드를 뜯어보면
# 지역 변수의 경우 STORE_FAST, 전역 변수의 경우 STORE_NAME이라는 명령어를 통해 저장이 되는데
# 이 문제의 경우 10! 이 넘는 저장 연산이 일어나서 전역변수, 지역변수의 차이가 어마무시하게 커진듯 싶다.
# 레퍼런스 : https://stackoverflow.com/questions/11241523/why-does-python-code-run-faster-in-a-function

# 접근 방식은 0번 도시부터 n-1번 도시까지 answer에 선언을 해주고
# 도시를 순환하는 모든 경우의 수를 순열을 통해 저장해 주었다.
# 그 경우의 수 대로 w 리스트를 활용해 비용을 계산했고
# 계산을 하는 도중 길이 끊겨 있거나, 이미 이전에 계산했던 비용보다 커지게 되는 경우에는 계산을 그만두고
# 다음 경우의 수로 넘어가는 방법을 사용하였다.

from itertools import permutations

def solved ():
    n = int(input())


    answer =[i for i in range(n)]
    w = []

    for i in range(n):
        w.append(list(map(int, input().split(' '))))


    answer = list(permutations(answer, n))
    temp = 1000000000

    for k in answer:
        value = 0
        check = True
        for j in range(len(k)):
            if j == (len(k) -1) :
                value = value + w[k[j]][k[0]]
                if w[k[j]][k[0]] == 0:
                    check = False
                    break
            else:
                value = value + w[k[j]][k[j+1]]
                if w[k[j]][k[j+1]] == 0:
                    check = False
                    break
            if value > temp:
                break
        if value < temp and check == True:
            temp = value

    print(temp)


solved()