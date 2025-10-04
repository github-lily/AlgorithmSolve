from collections import defaultdict

def solution(tickets):
    tickets.sort(reverse = True)
    
    route = []
    stack = ["ICN"]
    d = defaultdict(list)
    
    for a,b in tickets :
        d[a].append(b)
        
    # print(d)
    
    while stack :
        cur = stack[-1]

        if d[cur] :
            stack.append(d[cur].pop())
        else :
            route.append(stack.pop())
        
    return route[::-1]
            
    
        
    
    
    