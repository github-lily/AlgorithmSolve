N,M = map(int,input().split())

text_set = set()
ans = 0

# 집합 S에 포함된 문자열
for _ in range(N) :
    text = input()
    text_set.add(text)
    
# 확인해야할 문자열
for _ in range(M) :
    check_text = input()
    if check_text in text_set :
        ans += 1

print(ans)
