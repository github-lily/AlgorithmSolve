N = int(input())


# 5로 나누어떨어질 때
if N % 5  == 0 :
    print(N//5)

else :
    p = 0
    while N > 0 :
        N -= 3
        p += 1
        # 3과 5를 조합할 때
        if N % 5 == 0 :
            p += N//5
            print(p)
            break
        
        # 3과 5로 나눌 수 없을 때
        elif N == 1 or N == 2 :
            print(-1)
            break

        # 3으로 나누어 떨어질 때
        elif N == 0 :
            print(p)
            break