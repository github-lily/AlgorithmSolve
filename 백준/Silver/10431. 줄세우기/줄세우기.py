T = int(input())
for _ in range(T) :
    temp = list(map(int,input().split()))
    cnt = 0
    
    tc = temp[0]
    students = temp[1:]

    for i in range(20) :
        for j in range(i) :
            if students[j] > students[i] :
                cnt += 1

    print(tc, cnt)