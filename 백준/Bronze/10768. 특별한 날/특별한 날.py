M = int(input())
D = int(input())

if (M, D) < (2, 18):
    print("Before")
elif (M, D) == (2, 18):
    print("Special")
else:
    print("After")
