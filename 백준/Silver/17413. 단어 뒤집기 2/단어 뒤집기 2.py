sentence = input()

word = []
ans = []
is_tag = False

for s in sentence :
    # 태그
    if s == '<' :
        # 모아둔 단어 체크
        if word :
            ans.extend(reversed(word))
            word.clear()
        is_tag = True
        ans.append(s)
    
    elif s == '>' :
        is_tag = False
        ans.append(s)

    elif is_tag :
        ans.append(s)       # 태그 내부면 바로 넣기

    # 단어
    else :
        if s == ' ' :
            if word :
                ans.extend(reversed(word))
                word.clear()
            ans.append(s)
        else :
            word.append(s)

# 마지막 단어 넣기
if word :
    ans.extend(reversed(word))

print(''.join(ans))