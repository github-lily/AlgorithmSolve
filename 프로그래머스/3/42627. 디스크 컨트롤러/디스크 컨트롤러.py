import heapq as hq

def solution(jobs):
    q = []
    returnTime = 0
    now = 0
    idx = 0
    lenn = len(jobs)
    
    jobs.sort(key = lambda x : x[0])
    
    while idx < lenn or q :
    # 현재 시간까지 요청된 작업 모두 추가
        while idx < lenn and jobs[idx][0] <= now :
            hq.heappush(q, (jobs[idx][1], jobs[idx][0], idx))
            idx += 1
            
    
    # 대기중인 작업 처리
        if q :
            jt, st, i = hq.heappop(q)
            now += jt
            returnTime += (now - st)
    
    # 대기 중인 작업 없으면 시간 이동
        else :
            now = jobs[idx][0]
    
    return returnTime // lenn