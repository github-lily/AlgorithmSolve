from collections import deque

def solution(priorities, location):
    q = deque([(p, i) for i, p in enumerate(priorities)])
    answer = 0

    while q:
        cur = q.popleft()
        if any(cur[0] < q[0] for q in q):
            q.append(cur)
        else:
            answer += 1
            if cur[1] == location:
                return answer
