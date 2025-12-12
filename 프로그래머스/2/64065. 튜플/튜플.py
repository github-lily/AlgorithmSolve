def solution(s):
    s = s[2:-2]
    sets = s.split("},{")
    sets.sort(key=len)

    seen = set()
    answer = []

    for group in sets:
        for num in group.split(","):
            n = int(num)
            if n not in seen:
                seen.add(n)
                answer.append(n)
                break

    return answer
