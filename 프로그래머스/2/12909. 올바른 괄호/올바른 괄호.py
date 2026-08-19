def solution(s):
    stack = []
    lenn = len(s)
    
    for c in s :
        if c == ')' :
            if not stack :
                return False
            p = stack.pop()
            if p == c :
                return False
        else :
            stack.append(c)
    
    if stack :
        return False
    
    return True
            