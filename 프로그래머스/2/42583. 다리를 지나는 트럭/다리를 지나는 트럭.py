from collections import deque

'''
1. 0초엔 못올라감
2. 올라간 시간도 1초로 포함됨
3. 다리 길이만큼 시간이 걸림
'''
def solution(B, W, trucks):
    t = 0
    q = deque()
    nw = 0       # 현재 무게
    k = 0
    n = len(trucks)
    
    while True :    
        # 종료
        if k == n and not q :
            break
        
        # 다리 건너기 완료
        if q :
            # 현재시간 - 입장시간 >= B  : 트럭 내리기
            if t - q[0][0] >= B :
                nw -= q[0][1]
                q.popleft()

        # 다리 건너기 시작
        if k < n :
            tw = trucks[k]
            if nw + tw <= W :
                # 입장시간 추가. 현재시간 - 입장시간 >= B 빼기
                q.append((t, tw))
                nw += tw
                k += 1

        # 시간 증가
        t += 1
    
    return t