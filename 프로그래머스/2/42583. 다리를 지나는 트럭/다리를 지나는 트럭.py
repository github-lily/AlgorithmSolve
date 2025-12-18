from collections import deque

def solution(bl, w, tw):
    q = deque([0] * bl)     # 다리 위 
    tw = deque(tw)
    
    time = 0
    cw = 0
    
    while tw :
        time += 1
        cw -= q.popleft()

        # 무게기준을 넘지 않으면, 대기 트럭에서는 제거, 다리 위와 현재 무게에 추가
        if cw + tw[0] <= w :
            cw += tw[0]
            q.append(tw.popleft())
        
        # 무게 기준을 넘는다면 0 추가해서 한 칸 이동
        else :
            q.append(0)
        
    # tw가 비는 순간 = 마지막 트럭이 올라간 순간이므로, 마지막트럭이 이동할 시간만큼 추가
    time += bl
    
    return time
    
        
        