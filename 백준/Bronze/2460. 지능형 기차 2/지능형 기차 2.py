now = 0
max_now = 0

for _ in range(10) :
    minus, plus = list(map(int,input().split()))
    now -= minus
    now += plus
    if max_now < now :
        max_now = now

print(max_now)
