document = input()
word = input()

idx = 0
count = 0

while idx <= len(document) - len(word):
    if document[idx:idx+len(word)] == word:
        count += 1
        idx += len(word)  # 겹치지 않게 다음 인덱스로 이동
    else:
        idx += 1

print(count)
