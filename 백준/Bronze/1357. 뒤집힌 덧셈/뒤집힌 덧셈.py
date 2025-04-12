def reverse_number(n):
    return int(str(n)[::-1])

x, y = input().split()
x_reversed = reverse_number(x)
y_reversed = reverse_number(y)

result = reverse_number(x_reversed + y_reversed)
print(result)
