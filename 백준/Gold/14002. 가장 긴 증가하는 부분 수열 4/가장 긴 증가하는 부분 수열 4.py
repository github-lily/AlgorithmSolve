
N = int(input())
lst = [0] + list(map(int,input().split()))

dp = [0] * (N+1)
par = [0] * (N+1) # 부모 인덱스 저장 배열

for i in range(1,N+1) : # 확인해야할 수
    mx = 0
    for j in range(0,i) :  # 비교 구간
        if lst[i] > lst[j] :
            if dp[j] + 1 > dp[i] : # 최대길이가 더 긴경우
                dp[i] = dp[j] + 1
                par[i] = j

ans = max(dp)
ans_lst = []

idx = dp.index(ans) # 최대값이 저장되어있는 인덱스
for _ in range(ans) :
    ans_lst.append(lst[idx])
    idx = par[idx]

ans_lst.reverse()

print(ans)
print(*ans_lst)
