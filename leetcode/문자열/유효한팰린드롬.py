
def isPalindrome(s: str) -> bool:
    stack = []
    nums = ['0','1','2','3','4','5','6','7','8','9']
    for i in s:
        if i.isalpha():
            stack.append(i.upper())
    stack_2 = list(reversed(stack))

    for i in range(len(stack)):
        if not stack[i] == stack_2[i]:
            print('false')
            break
    else:
        print('true')
        

isPalindrome("0P")