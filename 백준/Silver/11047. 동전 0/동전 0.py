N, K = map(int,input().split())
cnt = 0
coins = []
for _ in range(N) :
    coins.append(int(input()))

# 그리디에 맞게 역순으로 출력
coins = sorted(coins, reverse=True)

for coin in coins :
    cnt += K // coin
    K %= coin

print(cnt)