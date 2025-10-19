def solution(n, s):
    ans = []
    
    if s < n :
        return [-1]
    
    elif s % n == 0 :
        num = s//n
        for _ in range(n) :
            ans.append(num)
        return ans
    
    else :
        num = s // n
        remain = s % n
        for _ in range(n) :
            if remain > 0 :
                ans.append(num+1)
                remain -= 1
            else :
                ans.append(num)
        ans.sort()
        return ans
