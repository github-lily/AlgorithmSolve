s = input()
target = "UCPC"
idx = 0

for char in s:
    if char == target[idx]:
        idx += 1
        if idx == 4:  # UCPC 다 찾았으면
            break

if idx == 4:
    print("I love UCPC")
else:
    print("I hate UCPC")
