name = input().strip()
n = int(input())
candidates = [input().strip() for _ in range(n)]

def love_score(name1, name2):
    counts = {'L':0,'O':0,'V':0,'E':0}
    for ch in name1+name2:
        if ch in counts:
            counts[ch] += 1
    L,O,V,E = counts['L'],counts['O'],counts['V'],counts['E']
    return ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E)) % 100

best_score = -1
best_name = ""
for c in sorted(candidates):
    score = love_score(name, c)
    if score > best_score:
        best_score = score
        best_name = c
print(best_name)
