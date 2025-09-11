import sys
input = sys.stdin.readline

N, M = map(int, input().split())

houses = []
chickens = []
for i in range(N):
    row = list(map(int, input().split()))
    for j, v in enumerate(row):
        if v == 1:
            houses.append((i, j))     # 0-index
        elif v == 2:
            chickens.append((i, j))

H = len(houses)
C = len(chickens)

# 1) 집-치킨 거리 테이블 사전 계산
dist = [[0] * C for _ in range(H)]
for h in range(H):
    hx, hy = houses[h]
    for c in range(C):
        cx, cy = chickens[c]
        d = hx - cx
        if d < 0: d = -d
        e = hy - cy
        if e < 0: e = -e
        dist[h][c] = d + e

INF = 10**9
ans = INF

# 2) 조합을 저장하지 않고 즉시 평가 (인덱스 조합, 고정배열 picked 사용)
picked = [0] * M  # 선택한 치킨 '인덱스'를 담음

def evaluate():
    """선택된 picked 조합으로 도시 치킨 거리 계산 (가지치기 포함)"""
    global ans
    total = 0
    for h in range(H):
        row = dist[h]
        best = INF
        # 선택된 치킨 중 최소 거리
        for k in range(M):
            d = row[picked[k]]
            if d < best:
                best = d
                if best == 1:  # 더는 줄일 수 없는 최솟값(미세 최적화)
                    break
        total += best
        if total >= ans:  # 가지치기
            return
    if total < ans:
        ans = total

def dfs(start, depth):
    """start부터 치킨 인덱스를 선택, depth개 선택 완료됨"""
    if depth == M:
        evaluate()
        return
    # 남은 슬롯을 채우기 위해 선택 가능한 최대 시작 인덱스 제한
    # (조합 불가능한 분기는 진입 자체 차단)
    limit = C - (M - depth) + 1
    for i in range(start, limit):
        picked[depth] = i
        dfs(i + 1, depth + 1)

if C == M:
    # 전부 선택하는 경우 한 번만 평가
    for i in range(M):
        picked[i] = i
    evaluate()
else:
    dfs(0, 0)

print(ans if ans < INF else 0)
