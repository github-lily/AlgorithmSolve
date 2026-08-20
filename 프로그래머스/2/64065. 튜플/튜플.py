def solution(s):
    a = s[2:-2].split("},{")

    a.sort(key=lambda x: len(x.split(",")))

    ans = []
    seen = set()

    for x in a:
        for n in map(int, x.split(",")):
            if n not in seen:
                seen.add(n)
                ans.append(n)

    return ans