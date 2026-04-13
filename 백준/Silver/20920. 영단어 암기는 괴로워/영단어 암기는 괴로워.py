import sys
input = sys.stdin.readline

N, M = map(int,input().split())
word_cnt = {}

# 사전에 단어 저장
for _ in range(N) :
    word = input().strip()
    if len(word) >= M :
        word_cnt[word] = word_cnt.get(word,0)+1

words = list(word_cnt.keys())

# 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다. (3순위)
words.sort()

# 해당 단어의 길이가 길수록 앞에 배치한다. (2순위)
words.sort(key = len, reverse= True)

# 자주 나오는 단어일수록 앞에 배치한다. (1순위)
words.sort(key = word_cnt.get, reverse=True)

print("\n".join(words))
