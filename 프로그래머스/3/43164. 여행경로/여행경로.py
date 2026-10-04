
def solution(tickets):
    
    places = dict()
    routes = ["ICN"]
    n = len(tickets)
    
    for start,end in tickets :
        if start not in places :
            places[start] = []
        places[start].append([end,1])
    
    for key in places :
        places[key].sort()
        
    isend = False
    
    def dfs(cur) :
        nonlocal isend
        
        
        if len(routes) == n + 1 :
            isend = True
            return
        
        if cur not in places :
            return 
        
        for nxt in places[cur] :
            if nxt[1] == 1 :
                nxt[1] = 0
                routes.append(nxt[0])
                
            
                dfs(nxt[0])
                
                if isend :
                    return
                
                nxt[1] = 1
                routes.pop()
    
    dfs("ICN")
    
    return routes
                
        