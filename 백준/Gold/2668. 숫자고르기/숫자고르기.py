
def dfs(s,c) :

    v[c] =  1
    n = nums[c]

    if v[n] == 0 :
        dfs(s,n)
    else :
        if s == n :     # 시작점과 끝점이 같음 == 사이클 발견
            ans.add(s)


N = int(input())
nums = [0]+[int(input()) for _ in range(N)]
ans = set()

for i in range(1,N+1) :
    v = [0] * (N+1)
    dfs(i,i)

print(len(ans))
for a in ans :
    print(a)
