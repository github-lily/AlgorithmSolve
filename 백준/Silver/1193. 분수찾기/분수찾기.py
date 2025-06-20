X = int(input())

line = 1
while X > line:
    X -= line
    line += 1

if line % 2 == 0:
    # 짝수줄: 분모 증가, 분자 감소
    a = X
    b = line - X + 1
else:
    # 홀수줄: 분자 증가, 분모 감소
    a = line - X + 1
    b = X

print(f"{a}/{b}")
