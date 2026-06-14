def solution(prices):
    stack = []
    N = len(prices)
    ans = [0] * N
    for i in range(N) :
        while stack and prices[stack[-1]] > prices[i] :
            prev = stack.pop()     # 가격이 떨어졌으면 제거
            ans[prev] = i - prev
        
        stack.append(i)

    
    while stack :
        cur = stack.pop()
        ans[cur] = N - 1 - cur
    
    return ans