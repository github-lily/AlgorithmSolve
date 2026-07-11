def check(c,t) :
    if (c == ']' and t == '[') or \
        (c == ')' and t == '(') or \
        (c == '}' and t == '{') :
        return True
    return False

def solution(s):
    open = ["[", "(", "{"]
    n = len(s)
    ans = n
    
    for i in range(n):
        stack = []
        for k in range(n) :
            idx = (i+k) % n
            cur = s[idx]
            if cur in open :
                stack.append(cur)
            else :
                if stack :
                    top = stack.pop()
                    if not check(cur, top) :
                        stack.append(top)
                        break
                else :  # 여는 괄호가 없을 때
                    ans -= 1
                    break
                    
        # 여는 괄호가 남았을 때
        if stack :
            ans -= 1

    return ans
    