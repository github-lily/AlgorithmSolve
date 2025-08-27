import sys
input = sys.stdin.readline

def find_right(c_idx, t):
    global q
    r_cnt = 0
    idx = c_idx
    while True:
        if q[idx] == t:
            return idx, r_cnt
        idx = (idx + 1) % len(q)
        r_cnt += 1

def find_left(c_idx, t):
    global q
    l_cnt = 0
    idx = c_idx
    while True:
        if q[idx] == t:
            return idx, l_cnt
        idx = (idx - 1 + len(q)) % len(q)
        l_cnt += 1

N, M = map(int, input().split())
targets = list(map(int, input().split()))
q = [x for x in range(1, N + 1)]
cur_idx = 0
ans = 0

for target in targets:
    if q[cur_idx] != target:
        if target < q[cur_idx]:
            t_idx, l_cnt = find_left(cur_idx, target)
            r_cnt = (t_idx - cur_idx) % len(q)
        else:
            t_idx, r_cnt = find_right(cur_idx, target)
            l_cnt = (cur_idx - t_idx) % len(q)

        ans += min(l_cnt, r_cnt)
        q.pop(t_idx)

        # 안전하게 cur_idx 보정
        if t_idx == len(q):  # pop한 인덱스가 마지막 원소였으면
            cur_idx = 0
        else:
            cur_idx = t_idx

    else:
        q.pop(cur_idx)
        if cur_idx == len(q):
            cur_idx = 0

print(ans)
