import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T) :
    N = int(input())        # 동전 종류 개수
    coins = list(map(int,input().split()))
    M = int(input())        # 동전으로 만들어야 할 금액

    dp = [0]*(M+1)
    dp[0] = 1

    for coin in coins :
        for j in range(M+1) :
            if j-coin >= 0 :
                dp[j] = dp[j] + dp[j-coin]
    
    print(dp[-1])