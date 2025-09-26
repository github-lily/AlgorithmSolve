def solution(n, lost, reserve):
    los = set(lost) - set(reserve)
    res = set(reserve) - set(lost)
    
    ans = n - len(los)

    for l in los :
        if l-1 in res :
            res.remove(l-1)
            ans += 1
        elif l+1 in res :
            res.remove(l+1)
            ans += 1
        
    return ans