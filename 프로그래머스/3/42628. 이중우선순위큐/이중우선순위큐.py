import heapq as hq

def solution(operations):
    mx_q = []
    mn_q = []
    N = len(operations)
    id_val = 0
    is_id = [0] * N
    
    for operation in operations :
        oper, num = operation.split()
        num = int(num)
        if oper == 'I' :
            hq.heappush(mn_q,(num, id_val))
            hq.heappush(mx_q,(-num, id_val))
            is_id[id_val] = 1
            id_val += 1
            
        else :
            if num == 1 :
                # q 동기화
                while mx_q and not is_id[mx_q[0][1]]:
                    hq.heappop(mx_q)
                
                if mx_q :
                    num, idv = hq.heappop(mx_q)
                    if is_id[idv] :
                        is_id[idv] -= 1
        
            else :
                # q 동기화
                while mn_q and not is_id[mn_q[0][1]] :
                    hq.heappop(mn_q)
                    
                if mn_q :
                    num, idv = hq.heappop(mn_q)
                    if is_id[idv] :
                        is_id[idv] -= 1
        
                    
            
                
    if sum(is_id) == 0 :
        return [0,0]
    
    while mx_q :
        num,idv = hq.heappop(mx_q)
        if is_id[idv] :
            mx = -num
            break
        
    while mn_q :
        num, idv = hq.heappop(mn_q)
        if is_id[idv] :
            mn = num
            break
    
    return [mx,mn]