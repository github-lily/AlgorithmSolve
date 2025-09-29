s = input().strip()
i = 0
ok = True
while i < len(s):
    if s.startswith("pi", i):
        i += 2
    elif s.startswith("ka", i):
        i += 2
    elif s.startswith("chu", i):
        i += 3
    else:
        ok = False
        break

print("YES" if ok else "NO")
