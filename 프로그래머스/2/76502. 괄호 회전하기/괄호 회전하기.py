def solution(s):
    answer = 0

    for i in range(len(s)):
        rotated = s[i:] + s[:i]
        stack = []
        valid = True

        for ch in rotated:
            if ch in "([{":
                stack.append(ch)
            else:
                if not stack:
                    valid = False
                    break

                top = stack.pop()

                if ch == ')' and top != '(':
                    valid = False
                    break
                if ch == ']' and top != '[':
                    valid = False
                    break
                if ch == '}' and top != '{':
                    valid = False
                    break

        if valid and not stack:
            answer += 1

    return answer