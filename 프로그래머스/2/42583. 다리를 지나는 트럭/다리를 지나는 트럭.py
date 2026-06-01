'''
트럭은 1초부터 올라간다
트럭은 1초에 다리 길이 1씩 전진한다.
트럭은 올라갈수 있으면 1초에 한 대씩 다리에 올라갈 수 있다
'''
from collections import deque

def solution(L, W, trucks):
    can = W             # 가능 무게
    wq = deque(trucks)  # 대기 큐
    pq = deque()        # 진행 큐
    time = 0               # 현재 시간

    
    while wq or pq:
        time += 1
        
        # 트럭 내리기
        if pq and (time - pq[0][1]) >= L :
            pw, pt = pq.popleft()
            time += L - (time - pt)
            can += pw
            
        # 새 트럭 올리기
        if wq and can >= wq[0] :
            c = wq.popleft()
            pq.append((c,time))
            can -= c

    return time
            
    
        
    
    