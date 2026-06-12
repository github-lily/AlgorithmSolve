def solution(prices):
    N = len(prices)
    stack = []
    ans = [0] * N
    
    for i in range(N-1,-1,-1) :
        now = prices[i]
        
        # 현재 가격보다 크거나 같은 값은 하락 지점이 될 수 없으므로 제거
        while stack and prices[stack[-1]] >= now :
            stack.pop()
            
        # 끝까지 작은 값이 안나온 경우
        if not stack :
            ans[i] = N-1-i
        
        # 처음으로 작은 값을 만난 경우
        else :
            ans[i] = stack[-1] - i
            
        
        # 현재 인덱스 추가
        stack.append(i)
        
    return ans

                
            