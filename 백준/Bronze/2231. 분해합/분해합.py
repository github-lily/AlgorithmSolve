def check() :
    for ans in range(n,N) :
        ans_str = str(ans)
        lenth = len(ans_str)
        num = ans
        # 자리수 더하기
        for i in range(lenth) :
            num += int(ans_str[i])
        
        # 일치하면 중단
        if num == N :
            return ans
    
    return 0
        


N = int(input())
M = len(str(N))     # 최대값
n = max(1, int(N) - 9*M)    # 최소값


ans = check()
print(ans)
