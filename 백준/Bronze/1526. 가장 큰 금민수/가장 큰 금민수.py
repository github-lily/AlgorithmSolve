n = int(input())
while True:
    if all(c in '47' for c in str(n)):
        print(n)
        break
    n -= 1
