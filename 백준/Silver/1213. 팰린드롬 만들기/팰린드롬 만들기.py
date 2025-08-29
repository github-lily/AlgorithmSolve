import sys
from collections import Counter

name = sys.stdin.readline().strip()
cnt = Counter(name)

odds = [ch for ch, c in cnt.items() if c % 2]
if len(odds) > 1:
    print("I'm Sorry Hansoo")
    sys.exit(0)

mid = odds[0] if odds else ''
left = []

for ch in sorted(cnt.keys()):
    left.append(ch * (cnt[ch] // 2))

left = ''.join(left)
print(left + mid + left[::-1])
