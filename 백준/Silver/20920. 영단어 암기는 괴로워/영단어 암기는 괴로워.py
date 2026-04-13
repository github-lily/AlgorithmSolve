import sys
input = sys.stdin.readline

N, M = map(int,input().split())
dict = {}

# 사전에 단어 저장
for _ in range(N) :
    word = input().strip()
    if len(word) >= M :
        if word in dict.keys() :
            dict[word] += 1
        else :
            dict[word] = 1
    
# 1. 자주 나오는 단어일수록 앞에 배치한다.
cnt = len(dict)
mx_cnt = max(dict.values())
words = [[] for _ in range(mx_cnt+1)]

for word,val in dict.items() :
    words[val].append(word)

ans = []

for i in range(mx_cnt,-1,-1) :
    lst = words[i]
    if lst :
        if len(lst) == 1 :
            ans.append(lst[0])
        else :
            # 2. 해당 단어의 길이가 길수록 앞에 배치한다.
            # 3. 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다.
            lst.sort(key = lambda x:(-len(x),x)) 
            ans.extend(lst)


print("\n".join(ans))