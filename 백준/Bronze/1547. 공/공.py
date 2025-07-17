cups = [0, 1, 2, 3]  # 인덱스 1~3 사용

for _ in range(int(input())):
    x, y = map(int, input().split())
    cups[x], cups[y] = cups[y], cups[x]

for i in range(1, 4):
    if cups[i] == 1:
        print(i)
        break
