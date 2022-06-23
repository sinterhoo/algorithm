from collections import deque

def strs(p):
    if p == '':
        return p
    u = []
    u_count_a = 0
    u_count_b = 0
    v = []
    
    p_list = deque(p)
    tmps = []
    while p_list:
        if len(tmps) == 0:
            tmps.append(p_list.popleft())
        else:
            if tmps[-1] == p_list[0]:
                break
            else:
                tmps.pop()
                p_list.popleft()
    else:
        return p
    for i in p:
        if u_count_a != 0 and u_count_a == u_count_b:
            if i == '(':
                u_count_a+=1
            else:
                u_count_b +=1
            u.append(i)
        else:
            v.append(i)
    else:
        s = ''.join(u)
        p_list = deque(s)
        tmps = []
        while p_list:
            if len(tmps) == 0:
                tmps.append(p_list.popleft)
            else:
                if tmps[-1] == p_list[0]:
                    break
                else:
                    tmps.pop()
                    p_list.popleft()
        else:
            temp = s + strs(v)
            return temp
        temp_u = deque(s)
        temp_u.popleft()
        temp_u.pop()
        for i in range(len(temp_u)):
            if temp_u[i] == '(':
                temp_u[i] = ')'
            else:
                temp_u[i] = '('
        
        temp_u.appendleft('(')
        temp_u.append(')')
        temp_u = list(temp_u)
        temp = ''.join(temp_u) + strs(v)
        
        return temp

def solution(p):
    answer = strs(p)
            
    return answer


print(solution("()))((()"))