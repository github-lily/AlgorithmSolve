N = int(input())
ans = 0
for _ in range(N) :
    text = input()
    n = len(text)

    # 한 글자인 경우
    if n == 1 :
        ans += 1

 
    # 한 글자 이상인 경우
    else :
        t_set = set(text[0])
        flag = True
        for i in range(1, len(text)) :
            if text[i] in t_set :               # 중복된 수가 나왔을 때
                if text[i-1] != text[i] :       # 이전값과 다르다면 중단
                    flag = False
                    break
            else :
                t_set.add(text[i])
        if flag == True :
            ans += 1
            

print(ans)