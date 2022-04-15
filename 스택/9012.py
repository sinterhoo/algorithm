
t = int(input())

string_list = [input() for _ in range(t)]


for i in string_list:
    check_stack = []
    for k in i:
        if k == '(':
            check_stack.append(k)
        else:
            if len(check_stack) == 0:
                print("NO")
                break
            else:
                check_stack.pop()
    else:
        if len(check_stack) == 0:
            print("YES")
        else:
            print("NO")
