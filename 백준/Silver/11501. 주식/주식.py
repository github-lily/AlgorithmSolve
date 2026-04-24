import sys
input = sys.stdin.readline

t = int(input())
result = []

for _ in range(t) :
    N = int(input())
    days = list(map(int,input().split()))
    
    ans = 0
    mx = days[-1]
    
    for i in range(N-1,-1,-1) :
        if mx < days[i] :
            mx = days[i]
        else :
            ans += mx - days[i]

    result.append(ans)


print("\n".join(map(str,result)))

        
