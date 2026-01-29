import sys
input = sys.stdin.readline

n = int(input())
lst = [int(input()) for _ in range(n)]

stack = []
num = 1
i = 0
result = []

while i < n:
    target = lst[i]

    # target이 나올 때까지 push
    while num <= target:
        stack.append(num)
        result.append('+')
        num += 1

    # 맨 위가 target이면 pop
    if stack[-1] == target:
        stack.pop()
        result.append('-')
        i += 1
    else:
        print("NO")
        sys.exit()
        
for r in result:
    print(r)
