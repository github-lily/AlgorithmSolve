s = input()
count0 = 0
count1 = 0

# 첫 글자 기준으로 카운트 시작
if s[0] == '0':
    count0 += 1
else:
    count1 += 1

# 연속된 숫자가 바뀔 때마다 카운트
for i in range(1, len(s)):
    if s[i] != s[i-1]:
        if s[i] == '0':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))
