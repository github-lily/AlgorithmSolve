arr = [input() for _ in range(5)]
max_len = max(len(row) for row in arr)

for i in range(5):
    arr[i] = arr[i].ljust(max_len)

for i in range(max_len):
    for j in range(5):
        if arr[j][i] != ' ':
            print(arr[j][i], end='')
