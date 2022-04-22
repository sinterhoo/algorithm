# 접근 방법 ->  1. 플러그가 비어있으면 채워준다
# 2. 플러그가 꽉 차 있으면 뒤의 모든 전자제품을 서치해 가장 늦게 나오거나 없는 전자제품의 플러그를 뽑는다.
# 3. 반복한다.

# 가능한 이유 -> 100 * 100 * 100 해봐야 100만의 연산! O(n^3)을 사용해도 충분하다
import sys


n,k = map(int, input().split())


nums = list(map(int, sys.stdin.readline().split()))
count = 0
stack = []
for i in range(k):
    if len(stack) < n:
        if not nums[i] in stack:
            stack.append(nums[i])
    else:
        if nums[i] in stack:
            continue
        else:
            temp = []
            for j in range(len(stack)):
                for m in range(i+1, k):
                    if stack[j] == nums[m]:
                        temp.append([m,j])
                        break
                else:
                    stack.pop(j)
                    stack.append(nums[i])
                    count +=1
                    break
            else:
                temp.sort(reverse=True)
                stack.pop(temp[0][1])
                stack.append(nums[i])
                count+=1

print(count)