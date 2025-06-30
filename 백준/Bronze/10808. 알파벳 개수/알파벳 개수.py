word = input()
count = [0] * 26

for ch in word:
    count[ord(ch) - ord('a')] += 1

print(' '.join(map(str, count)))
