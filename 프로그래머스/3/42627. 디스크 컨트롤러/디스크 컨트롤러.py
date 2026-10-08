import heapq as hq

def solution(jobs):
    lenn = len(jobs)
    waitingQ = []
    now = 0
    returnTime = 0

    jobs.sort(key=lambda x: x[0])

    # 다음에 큐에 삽입할 작업 인덱스
    idx = 0

    # 모든 작업이 처리될 때까지 반복
    while idx < lenn or waitingQ:

        # 현재 시각까지 요청된 작업을 모두 삽입
        while idx < lenn and jobs[idx][0] <= now:
            startTime, jobTime = jobs[idx]
            hq.heappush(waitingQ, (jobTime, startTime, idx))
            idx += 1

        # 대기 중인 작업이 있다면 실행
        if waitingQ:
            j, s, i = hq.heappop(waitingQ)
            now += j
            returnTime += (now - s)

        # 대기 중인 작업이 없다면 다음 요청 시각으로 이동
        else:
            now = jobs[idx][0]

    return returnTime // lenn