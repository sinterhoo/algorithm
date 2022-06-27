def solution(board, moves):
    answer = 0
    stack = [[] for _ in range(len(board)+1)]
    
    answer_stack = []
    
    board = board[::-1]
    
    for i in range(len(board)):
        for k in range(len(board[i])):
            if not board[i][k] == 0:
                stack[k+1].append(board[i][k])
                
    for i in moves:
        if len(answer_stack) == 0:
            if len(stack[i]) != 0:
                answer_stack.append(stack[i].pop())
        else:
            if len(stack[i]) == 0:
                continue
            temp = stack[i].pop()
            if temp == answer_stack[-1]:
                answer_stack.pop()
                answer +=1
            else:
                answer_stack.append(temp)
    
    print(stack)
    
    return answer


print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))