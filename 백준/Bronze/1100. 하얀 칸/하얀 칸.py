chess = [list(input()) for _ in range(8)]


# 하얀칸
# i가 짝수일 때 j도 짝수인 곳
# i가 홀수일 때 j도 홀수인 곳
ans = 0

for i in range(8) :
    for j in range(8) :
        is_odd_j = j % 2
        # 짝수일 때
        if i % 2 == 0 :
            if is_odd_j == 0 and chess[i][j] == "F" :
                ans += 1
        # 홀수일 때
        else :
            if is_odd_j == 1 and chess[i][j] == "F" :
                ans += 1

print(ans)
             