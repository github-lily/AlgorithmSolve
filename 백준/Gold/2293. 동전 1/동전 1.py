import sys
input = sys.stdin.readline

n,k = map(int,input().split())
coins = []
for _ in range(n) :
    coins.append(int(input()))

money = [0]*(k+1)
money[0] = 1

for coin in coins :
    for i in range(1,k+1) :
        if i-coin >= 0 :
            money[i] += money[i-coin]

print(money[-1])