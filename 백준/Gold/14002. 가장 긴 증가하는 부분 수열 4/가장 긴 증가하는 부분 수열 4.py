N = int(input())
lst = [0] + list(map(int,input().split()))

dp = [0] * (N+1)

for i in range(1,N+1) : # 확인해야할 수
    mx = 0
    for j in range(0,i) :  # 비교 구간
        if lst[i] > lst[j] :
            mx = max(mx,dp[j])
    dp[i] = mx + 1

ans = max(dp)
ans_lst = [0] * ans 

idx = ans
for k in range(N, -1,-1) :
    if dp[k] == idx :
        ans_lst[idx-1] = lst[k]
        idx -= 1

        if idx == 0 :
            break

        
    
print(ans)
print(*ans_lst)