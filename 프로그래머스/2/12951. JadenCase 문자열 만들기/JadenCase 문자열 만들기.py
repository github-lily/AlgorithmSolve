def solution(s):
    ans = []
    for word in s.split(" "):
        if word:
            ans.append(word[0].upper() + word[1:].lower())
        else:
            ans.append("")
    return " ".join(ans)
