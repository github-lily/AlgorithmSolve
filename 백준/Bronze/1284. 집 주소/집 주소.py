while True:
    num = input()
    if num == '0':
        break

    width = 1  # 맨 앞 여백
    for digit in num:
        if digit == '1':
            width += 2
        elif digit == '0':
            width += 4
        else:
            width += 3
        width += 1  # 숫자 사이 여백

    print(width)
