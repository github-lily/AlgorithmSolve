
text = input()
N = len(text)
i = 0
cnt = 0
char = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
while i < N :
    word1 = text[i:i+2]
    word2 = text[i:i+3]


    if word2 in char :
        cnt += 1
        i += 3

    
    elif  word1 in char :
        cnt += 1
        i += 2



    else :
        cnt += 1
        i += 1

    
print(cnt)
        