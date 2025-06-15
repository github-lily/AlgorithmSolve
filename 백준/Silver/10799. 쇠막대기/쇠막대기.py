s = input()
stack = []
result = 0

for i in range(len(s)):
    if s[i] == '(':
        stack.append('(')
    else:  # ')'
        stack.pop()
        if s[i-1] == '(':  # 레이저
            result += len(stack)
        else:  # 막대기의 끝
            result += 1

print(result)
