while True:
    n = input()
    if n == '0':
        break
    width = 1  # 맨 앞 여백
    for digit in n:
        if digit == '1':
            width += 2
        elif digit == '0':
            width += 4
        else:
            width += 3
        width += 1  # 각 숫자 뒤 여백 추가
    print(width)
