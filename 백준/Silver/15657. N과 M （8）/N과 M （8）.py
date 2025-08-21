import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
result = []

def backtrack(start, seq):
    if len(seq) == m:
        print(*seq)
        return
    for i in range(start, n):
        # i부터 시작하므로 같은 수 중복 가능
        backtrack(i, seq + [nums[i]])  
        

backtrack(0, [])
