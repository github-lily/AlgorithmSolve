def check() :
    global word, N, half
    if N % 2 == 0 :
        for i in range(half) :
            if word[half-i] != word[half+i-1] :
                return 0

    else :
        for i in range(1,half+1) :
            if word[half-i] != word[half+i] :
                return 0
            
    return 1


word = input()
N = len(word)
half = N // 2

ans = check()
print(ans)