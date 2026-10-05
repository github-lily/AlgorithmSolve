import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0

    while len(scoville) >= 2 and scoville[0] < K:
        # 가장 맵지 않은 두 음식 추출
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)

        # 새 스코빌 지수 추가
        heapq.heappush(scoville, first + second * 2)
        answer += 1

    if scoville[0] < K:
        return -1

    return answer