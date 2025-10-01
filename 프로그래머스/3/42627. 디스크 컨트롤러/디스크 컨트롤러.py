import heapq as hq

def solution(jobs):
    q = []
    i = 0
    now = 0
    return_time = 0 
    n = len(jobs)
    
    jobs.sort(key = lambda x :x[0])     # 요청시간순으로 정렬
    

    while i < n or q :
        while i < n and jobs[i][0] <= now :     # 현재시간보다 요청시간이 빠른경우 q에 넣기
            # 작업의 소요시간이 짧은 것, 작업의 요청 시각이 빠른 것, 작업의 번호가 작은 것 순으로 우선순위
            # 순서대로 대기 큐에 넣기
            hq.heappush(q,(jobs[i][1],jobs[i][0]))
            i += 1
                        
            
        # 우선순위가 높은거 먼저 꺼내기
        if q :
            task = hq.heappop(q)
            now += task[0]                      # 작업 실행
            return_time += (now - task[1])      # 반환시간 더하기
            
        else :
            now = jobs[i][0]                   # 다음 작업 시간으로 점프

    # 개수만큼 나눠서 return
    ans = return_time // len(jobs)
    return ans
    
