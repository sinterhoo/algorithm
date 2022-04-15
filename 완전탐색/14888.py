# 문제 링크 : https://www.acmicpc.net/problem/14888

# 맨 처음 코드는 시간 초과가 났는데 중복을 제거하지 않아서 불필요한 연산이 너무 많았음
# ex) 뺄셈1 뺄셈2 나눗셈 , 뺄셈2 뺄셈1 나눗셈 모두 연산을 하다보니 초과가 떴음
# set을 이용해 중복을 제거해줬음


from itertools import permutations

def solved():
    n = int(input())

    nums = list(map(int, input().split(' ')))

    operator = list(map(int, input().split(' ')))

    answer = []

    for i in range(4):
        while operator[i] > 0:
            answer.append(i)
            operator[i] = operator[i] - 1

    answer = list(permutations(answer, n-1))
    my_set = set(answer)
    answer = list(my_set)

    minNums = 1100000000
    maxNums = -1100000000

    for i in answer:
        value = 0
        for k in range(n-1):
            if k == 0 :
                value = nums[0]
            if i[k] == 0:
                value = value + nums[k+1] 
            elif i[k] == 1:
                value = value - nums[k+1]
            elif i[k] == 2:
                value = value * nums[k+1]
            else:
                value = int(value / nums[k+1])
        if value > maxNums:
            maxNums = value
        if value < minNums:
            minNums = value


    print(maxNums)
    print(minNums)

solved()