# 입력 받기
S1, S2, S3 = map(int, input().split())

# 가능한 합의 개수를 저장할 딕셔너리
count = {}

# 세 주사위의 모든 합 계산
for i in range(1, S1 + 1):
    for j in range(1, S2 + 1):
        for k in range(1, S3 + 1):
            total = i + j + k
            if total in count:
                count[total] += 1
            else:
                count[total] = 1

# 가장 많이 나오는 합 중 가장 작은 값 찾기
max_count = max(count.values())
result = min([key for key, value in count.items() if value == max_count])

print(result)
