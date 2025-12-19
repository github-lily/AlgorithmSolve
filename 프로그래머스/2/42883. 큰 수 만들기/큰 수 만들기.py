def solution(numbers, k):
    stack = []
    for num in numbers :
        while stack and k > 0 and num > stack[-1] :
            stack.pop()
            k -= 1
        stack.append(num)

    
    if k :
        ans = "".join(stack[:-k])
    else :
        ans = "".join(stack)
    
    return ans


    
