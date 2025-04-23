
while True :
    # 길이값 오름차순 정렬렬
    length = sorted(map(int,input().split()))

    if sum(length) == 0 :
        break

    a = length[0]
    b = length[1]
    c = length[2]

    # 분기
    if a == b == c :
        print("Equilateral")
    elif a + b <= c :
        print("Invalid")
    elif a == b != c or a != b == c or a == c != b :
        print("Isosceles")
    else :
        print("Scalene")
