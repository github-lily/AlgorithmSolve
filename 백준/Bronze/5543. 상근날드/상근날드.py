mn_b = 2001
mn_d = 2001

# 버거 최솟값
for _ in range(3) :
    p = int(input())
    if p < mn_b :
        mn_b = p

# 음료 최솟값
for _ in range(2) :
    p = int(input())
    if p < mn_d :
        mn_d = p

print(mn_b + mn_d - 50)