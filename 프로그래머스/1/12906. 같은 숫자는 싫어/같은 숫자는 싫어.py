def solution(arr):
    stack = []
    stack.append(arr[0])
    top = 0
    for i in range(1,len(arr)) :
        if stack[top] != arr[i] :
            stack.append(arr[i])
            top += 1
    
    return stack