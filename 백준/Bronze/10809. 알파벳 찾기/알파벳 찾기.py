text = input()
cnt = [-1] * 26

for idx,char in enumerate(text) :
    cur = ord(char) - ord('a')
    if cnt[cur] == -1 :
        cnt[cur] = idx

print(*cnt)