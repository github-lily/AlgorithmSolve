import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T) :
    N = int(input())
    wardrobe = {}
    for _ in range(N) :
        clothes,kind = input().split()
        wardrobe[kind] = wardrobe.get(kind,0) + 1


    # (종류별 옷의 개수 + 1)을 모두 곱한 뒤 전혀 안입는 경우 -1
    # +1을 더하는 이유는 전혀 안입을 수도 있기 때문
    ans = 1
    for value in wardrobe.values() :
        ans *= (value +1)

    print(ans-1)


