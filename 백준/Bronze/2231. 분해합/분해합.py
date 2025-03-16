N = int(input())

# 가능한 생성자의 최소 범위 설정
start = max(0, N - 9 * len(str(N)))

# 브루트포스 탐색
for num in range(start, N):
    temp, digit_sum = num, 0

    # 각 자리수 합 계산
    while temp:
        digit_sum += temp % 10
        temp //= 10

    if num + digit_sum == N:
        print(num)
        break
else:
    print(0)
