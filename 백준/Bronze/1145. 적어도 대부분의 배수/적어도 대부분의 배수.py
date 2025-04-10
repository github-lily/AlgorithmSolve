nums = list(map(int, input().split()))

i = 1
while True:
    count = 0
    for num in nums:
        if i % num == 0:
            count += 1
    if count >= 3:
        print(i)
        break
    i += 1
