import heapq as hq

def solution(operations):
    mx_q = []
    mn_q = []
    id_dict = dict()
    id = 0

    for com in operations:
        c, n = com.split()
        n = int(n)

        if c == "I":
            hq.heappush(mn_q, (n, id))
            hq.heappush(mx_q, (-n, id))  # 최대힙: 부호 반전
            id_dict[id] = True
            id += 1

        elif c == "D":
            if n == -1:  # 최솟값 삭제
                # 이미 무효화된 top 정리
                while mn_q and not id_dict.get(mn_q[0][1], False):
                    hq.heappop(mn_q)
                if mn_q:
                    _, cid = hq.heappop(mn_q)
                    id_dict[cid] = False
            elif n == 1:  # 최댓값 삭제
                while mx_q and not id_dict.get(mx_q[0][1], False):
                    hq.heappop(mx_q)
                if mx_q:
                    _, cid = hq.heappop(mx_q)
                    id_dict[cid] = False

    # 최종 정리
    while mn_q and not id_dict.get(mn_q[0][1], False):
        hq.heappop(mn_q)
    while mx_q and not id_dict.get(mx_q[0][1], False):
        hq.heappop(mx_q)

    if not mn_q or not mx_q:
        return [0, 0]

    mn = mn_q[0][0]
    mx = -mx_q[0][0]  # 부호 되돌리기
    return [mx, mn]
