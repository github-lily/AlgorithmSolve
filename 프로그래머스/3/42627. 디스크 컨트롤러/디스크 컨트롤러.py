import heapq as hq

# 문맥교환에 걸리는 시간 X
def solution(jobs):
    wait_q = []
    n = len(jobs)
    times = [0] * n     # 반환시간 저장
    time = 0
    idx = 0

    # jobs 요청 시각 순 정렬
    jobs.sort(key = lambda x : x[0])
    
    while wait_q or idx < n :
        # 요청 시각 되면 대기 큐 삽입
        while idx < n and time >= jobs[idx][0] :
            # 소요시간, 요청시각, 작업번호 순 우선순위
            hq.heappush(wait_q, (jobs[idx][1], jobs[idx][0], idx))
            idx += 1
        
        # 우선순위에 맞게 꺼내기
        if wait_q :
            LT, RT, ID = hq.heappop(wait_q)
            time += LT              # 실행
            times[ID] = time - RT   # 반환시간 = 현재시간(완료시각) - 요청시각
        else :
            time += 1               # 꺼낼거 없으면 시간 추가
            
    
    ans = sum(times) // n
    return ans

        
    
    
    