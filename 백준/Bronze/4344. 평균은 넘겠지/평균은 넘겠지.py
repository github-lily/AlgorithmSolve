import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T) :
    lst = list(map(int,input().split()))
    N = lst[0]
    vals = lst[1:]
    sum_val = sum(vals)
    avg_val = sum_val/N

    up = 0
    for val in vals :
        if val > avg_val :
            up += 1

    ans = (up/N)*100

    print(f"{ans:.3f}%")