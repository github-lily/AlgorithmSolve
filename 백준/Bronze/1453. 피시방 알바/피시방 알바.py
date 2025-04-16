N = int(input())
seat = list(map(int,input().split()))

seat_set = set(seat)

ans = len(seat) - len(seat_set)
print(ans)
