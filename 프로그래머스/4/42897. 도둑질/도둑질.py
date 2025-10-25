def solution(money):
    n = len(money)

    def rob(arr):
        dp = [0] * len(arr)
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])
        for i in range(2, len(arr)):
            dp[i] = max(dp[i-1], dp[i-2] + arr[i])
        return dp[-1]

    # 1) 첫 집을 털고 마지막 집은 제외
    case1 = rob(money[:-1])

    # 2) 첫 집을 털지 않고 마지막 집 포함
    case2 = rob(money[1:])

    return max(case1, case2)
