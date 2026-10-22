
def solution(s):
    answer = 0
    pairs = {')': '(', ']': '[', '}': '{'}

    for i in range(len(s)):
        rotated = s[i:] + s[:i]
        stack = []

        for ch in rotated:
            if ch in '([{':
                stack.append(ch)
            elif not stack or stack.pop() != pairs[ch]:
                break
        else:
            if not stack:
                answer += 1

    return answer
