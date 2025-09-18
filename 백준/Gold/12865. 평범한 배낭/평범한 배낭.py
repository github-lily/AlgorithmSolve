

N,K = map(int,input().split())

items = []
for _ in range(N) :
    W,V = map(int,input().split())
    items.append([W,V])

# item 리스트 정렬
items.sort(key=lambda x : x[0])



# 1차원 dp 테이블
dp = [0] * (K+1)


for i in range(1, N+1) :       # 물건
    w,v = items[i-1]             # 역순으로 해야 값이 덮어씌여진 값으로 더해져 오류나는 것을 방지할 수 있음
    for j in range(K, w-1, -1) : # 무게 : 최대무게~ 현재무게까지 역순으로 확인.
        dp[j] = max(dp[j], dp[j-w]+v)   # 현재 저장된 값 vs (현재무게-현재물건무게)의 가치 + 현재물건의 가치                     
        
print(dp[K])
