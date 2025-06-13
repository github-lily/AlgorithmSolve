from itertools import combinations

while True:
    nums = list(map(int, input().split()))
    if nums[0] == 0:
        break
    for comb in combinations(nums[1:], 6):
        print(*comb)
    print()
