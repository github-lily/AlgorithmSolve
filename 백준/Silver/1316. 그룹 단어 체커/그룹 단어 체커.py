N = int(input())
cnt = 0
for _ in range(N) :
    text = input()
    char = set()
    
    i = 0
    flag = True

    while i < len(text) :
        cur = text[i]
        if text[i] in char :
            flag = False
            break
        char.add(text[i])
        i += 1
        while i < len(text) :
            next = text[i]
            if cur != next :
                break
            i += 1
    
    if flag :
        cnt += 1

print(cnt)