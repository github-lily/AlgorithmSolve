def solution(string):
    stack = []
    for s in string :
        if s == '(' :
            stack.append(s)
        else :
            if not stack :
                return False
            x = stack.pop()
            if x == ')' :
                return False
            
    if stack :
        return False
    return True