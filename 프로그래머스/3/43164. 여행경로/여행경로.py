def solution(tickets):
    n = len(tickets)
    tickets.sort()      # 알파벳 순서대로
        
    used = [False] * n
    ans = ['ICN']
    
    
    def dfs(cur) :
        nonlocal ans
        # 티켓 모두 사용시 종료
        if len(ans) == n+1 :
            return True
        
        for i in range(n) :
            start,end = tickets[i]
            
            if cur == start and not used[i] :
                used[i] = True
                ans.append(end)
                
                if dfs(end) :
                    return True
                
                # 티켓 다 못쓰면 초기화
                ans.pop()
                used[i] = False
                
                
        return False
    
    dfs('ICN')
    
    return ans
        
    
    

    
        