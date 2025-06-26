N, new_score, P = map(int, input().split())

if N > 0:
    scores = list(map(int, input().split()))
else:
    scores = []

rank = 1  # 기본 등수

for i in range(N):
    if scores[i] > new_score:
        rank += 1
    elif scores[i] == new_score:
        continue
    else:
        break

if N == P and (N > 0 and scores[-1] >= new_score):
    print(-1)
else:
    print(rank)
