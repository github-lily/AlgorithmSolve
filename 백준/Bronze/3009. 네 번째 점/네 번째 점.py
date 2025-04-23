x_list = []
y_list = []

for _ in range(3):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

# x 좌표 중 하나만 등장하는 값 찾기
for x in x_list:
    if x_list.count(x) == 1:
        fourth_x = x
        break

# y 좌표 중 하나만 등장하는 값 찾기
for y in y_list:
    if y_list.count(y) == 1:
        fourth_y = y
        break

print(fourth_x, fourth_y)
