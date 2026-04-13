
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
dict = {}

# 사전에 단어 저장
for _ in range(N) :
    word = input().strip()
    if len(word) >= M :
        dict[word] = dict.get(word,0)+1

ans = list(dict.keys())

'''
정렬 조건
1. 자주 나오는 단어일수록 앞에 배치한다.
2. 해당 단어의 길이가 길수록 앞에 배치한다.
3. 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다
'''
ans.sort(key = lambda x : (-dict[x], -len(x),x))

print("\n".join(ans))