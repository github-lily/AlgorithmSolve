T = int(input())
for _ in range(T) :
    k = int(input())
    n = int(input())

    dp = [0] * n
    for w in range(1,n+1) :
        dp[w-1] = w

    for _ in range(1, k+1) :
        for i in range(1,n) :
            dp[i] += dp[i-1]

    
    print(dp[n-1])