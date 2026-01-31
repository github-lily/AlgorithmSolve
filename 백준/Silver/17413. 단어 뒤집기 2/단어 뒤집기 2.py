
text = list(input())

s = 0
e = 0
n = len(text)
ans = ''

while e < n :
    # 태그일 때 건너뛰기
    if text[e] == '<' :     # 태그 시작
        if s != e :         # 그동안 모아둔 단어가 있다면 뒤집기
            ans += ''.join(text[s:e][::-1])
            s = e           # 태그 시작으로 시작점 이동 

        # 태그 끝 찾기
        while e < n and text[e] != '>' :
            e += 1
        
        # 태그 붙이기
        ans += ''.join(text[s:e+1])
        s = e +1

    # 단어 뒤집기(공백은 단어 끝 의미)
    elif text[e] == ' ' :
        ans += ''.join(text[s:e][::-1])
        ans += ' '
        s = e + 1       # 시작 재설정
    
    # 문장 끝
    elif e == n-1 :
        ans += ''.join(text[s:e+1][::-1])
    
    e += 1

print(ans)


