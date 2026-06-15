import heapq as hq

def solution(operations):
    mn_q = []
    mx_q = []
    cnt = {}
    
    def clear_mn() :
        while mn_q and cnt.get(mn_q[0],0) == 0 :
            hq.heappop(mn_q)
    
    def clear_mx() :
        while mx_q and cnt.get(-(mx_q[0]),0) == 0 :
            hq.heappop(mx_q)
    
    for opration in operations :
        opr, num = opration.split()
        num = int(num)
        
        if opr == 'I' :
            hq.heappush(mn_q,num)
            hq.heappush(mx_q,-num)
            cnt[num] = cnt.get(num, 0) + 1
            
        else :
            # 최댓값
            if num == 1 :
                clear_mx()
                if mx_q :                
                    x = -(hq.heappop(mx_q))
                    cnt[x] -= 1

            # 최소값
            else :
                clear_mn()
                if mn_q :
                    x = hq.heappop(mn_q)
                    cnt[x] -= 1
    
    
    clear_mx()
    clear_mn()
    
    if mn_q :
        return [-mx_q[0], mn_q[0]]
    
    else :
        return [0,0]
            