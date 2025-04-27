import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())

v = [0] * (N+1)
tree = [[] for _ in range(N+1)]
p = [0] * (N+1)

for _ in range(N-1):  # range(1, N) 말고 range(N-1)!!
    n1, n2 = map(int, sys.stdin.readline().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

def dfs(num):
    v[num] = 1
    for i in tree[num]:
        if v[i] == 0:
            p[i] = num
            dfs(i)

dfs(1)

for i in range(2, N+1):
    print(p[i])
