
T = int(input())
for _ in range(T) :
    words = input()
    K = int(input())

    idxs = [[] for _ in range(26)]
    mn = 100001
    mx = 0

    for i, word in enumerate(words) :
        cur = ord(word) - 97
        idxs[cur].append(i)

    for idx in idxs :
        for i in range(len(idx)-K+1) :
            length = idx[i+K-1] - idx[i] + 1
            mn = min(mn,length)
            mx = max(mx,length)

    if mn == 100001 and mx == 0 :
        print(-1)
    else :
        print(mn, mx)
