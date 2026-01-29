import sys
input = sys.stdin.readline

n = int(input())
target = list(int(input()) for _ in range(n))

i = 0   # target
num = 1 # 1~n (오름차순)

stack = []
out = []

ok = True   # flag

while i < n and ok :
    t = target[i]
    
    # target number까지 숫자 push
    while num <= t :
        stack.append(num)
        out.append('+')
        num += 1

    # t와 일치하면 pop
    if stack and stack[-1] == t :
        stack.pop()
        out.append('-')
        i += 1
    # 일치하지 않으면 즉시 중단 (불일치 == t < stack[-1] : 더 큰 수로 덮여 못나옴)
    else :
        ok = False

if ok :
    print("\n".join(out))
else :
    print("NO")
    