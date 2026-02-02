
N = int(input())
ans = []

for _ in range(N) :
    PS = list(input())
    stack = []
    is_vps = True        #

    for ps in PS :
        if ps == '(' :
            stack.append(ps)
        else :      # )
            if stack :
                stack.pop()
            else :      # 닫힌 괄호인데 스택이 비어있으면
                is_vps = False
                break

    # 다 돌았는데 stack에 남은 값이 있으면
    # 또는 is_vps가 false라면
    if stack or not is_vps:
        ans.append('NO')
    else :
        ans.append('YES')

print('\n'.join(ans))