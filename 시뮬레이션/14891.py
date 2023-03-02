from collections import deque


wheel1 = deque(list(input()))
wheel2 = deque(list(input()))
wheel3 = deque(list(input()))
wheel4 = deque(list(input()))

# 바퀴 목록
wheels = [wheel1,wheel2,wheel3,wheel4]
# 바퀴가 회전했는지 check하는 list
check = [0,0,0,0]

# 회전 로직
def rotate_wheel(start,nums, dir, compare_right, compare_left):
    # 시작 바퀴일 경우
    if check[nums] == 0:
        wheels[nums].rotate(dir)
        check[nums] = 1
    if nums == 0:
        if compare_right != wheels[nums+1][6] and check[nums+1] == 0:
            temp_right = wheels[nums+1][2]
            temp_left = wheels[nums+1][6]
            wheels[nums+1].rotate(dir*(-1))
            check[nums+1] = 1
            rotate_wheel(start,nums+1, dir*(-1),temp_right,temp_left)
    elif nums == 3:
        if compare_left != wheels[nums-1][2] and check[nums-1] == 0:
            temp_right = wheels[nums-1][2]
            temp_left = wheels[nums-1][6]
            wheels[nums-1].rotate(dir*(-1))
            check[nums-1] = 1
            rotate_wheel(start,nums-1,dir*(-1),temp_right,temp_left)
    else:
        if compare_right != wheels[nums+1][6] and check[nums+1] == 0:
            temp_right = wheels[nums+1][2]
            temp_left = wheels[nums+1][6]
            wheels[nums+1].rotate(dir*(-1))
            check[nums+1] = 1
            rotate_wheel(start,nums+1,dir*(-1),temp_right,temp_left)
        if compare_left != wheels[nums-1][2] and check[nums-1] == 0:
            temp_right = wheels[nums-1][2]
            temp_left = wheels[nums-1][6]
            wheels[nums-1].rotate(dir*(-1))
            check[nums-1] = 1
            rotate_wheel(start,nums-1,dir*(-1),temp_right,temp_left)

k = int(input())

for _ in range(k):
    number, direct = map(int, input().split())
    number -= 1

    rotate_wheel(number,number,direct,wheels[number][2], wheels[number][6])
    check = [0,0,0,0]

answer = int(wheels[0][0])*1 + int(wheels[1][0])*2 + int(wheels[2][0])*4 + int(wheels[3][0])*8

print(answer)