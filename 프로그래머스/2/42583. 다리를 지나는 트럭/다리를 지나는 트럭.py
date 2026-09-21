from collections import deque

def solution(bridge_length, limit, truck_weights):
    N = len(truck_weights)
    q = deque([(truck_weights[0],1)])
    cnt = 1
    weight = truck_weights[0]
    now = 2
    i = 1
    
    while True :
        if i == N and not q :
            break
        
        # 하차
        # 현재시간 - 시작시간
        if (now - q[0][1]) == bridge_length :
            w,s = q.popleft()
            cnt -= 1
            weight -= w
            
        # 승차
        # 마지막 트럭 고려
        if i < N and bridge_length > cnt and (weight + truck_weights[i]) <= limit :
            w = truck_weights[i]
            q.append((w,now))
            cnt += 1
            weight += w
            i += 1
        
        now += 1
        
    return now -1
        
        
        
    
                
                
            
            
    