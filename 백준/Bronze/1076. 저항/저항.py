# 색상 코드 매핑
color_codes = {
    "black": (0, 1),
    "brown": (1, 10),
    "red": (2, 100),
    "orange": (3, 1000),
    "yellow": (4, 10000),
    "green": (5, 100000),
    "blue": (6, 1000000),
    "violet": (7, 10000000),
    "grey": (8, 100000000),
    "white": (9, 1000000000),
}

# 입력 받기
first = input().strip()
second = input().strip()
third = input().strip()

# 저항 값 계산
value = color_codes[first][0] * 10 + color_codes[second][0]
multiplier = color_codes[third][1]
result = value * multiplier

# 출력
print(result)
