import math

def solution(p, s):
    ans = []
    left_d = []
    # 남은 날 구하기
    for i in range(len(p)) :
        moc = math.ceil((100-p[i])/s[i])
        left_d.append(moc)
    
    # 더 큰 수 나올때까지 +
    while left_d :
        cur = left_d.pop(0)
        result = 1
        while left_d and cur >= left_d[0] :
            result += 1
            left_d.pop(0)
        ans.append(result)
    
    return ans