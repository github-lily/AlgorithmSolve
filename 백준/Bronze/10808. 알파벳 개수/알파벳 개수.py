text = input()
cnt = [0] * 26

for char in text :
    cnt[ord(char) - ord('a')] += 1

print(*cnt)
