def solution(s):
    answer = True
    stack = []
    
    for word in s:
        if word == '(':
            stack.append(word)
        else:
            if len(stack) == 0:
                answer = False
                break
            if stack[-1] == '(':
                stack.pop()
    
    if len(stack) != 0:
        answer = False

    return answer