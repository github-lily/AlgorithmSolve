
def tournament_round(n, m):
    round_cnt = 0

    while n != m:
        n = (n + 1) // 2
        m = (m + 1) // 2
        round_cnt += 1

    return round_cnt

length, n, m = map(int, input().split())

print(tournament_round(n, m))
