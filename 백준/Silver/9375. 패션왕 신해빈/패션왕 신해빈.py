import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T) :
    N = int(input())
    wardrobe = dict()
    for _ in range(N) :
        clothes,kind = input().split()
        if kind in wardrobe :
            wardrobe[kind] += 1
        else :
            wardrobe[kind] = 1

    # 같은 종류의 옷이라면 1번씩 입는 경우만 가능
    if len(wardrobe.keys()) == 1 :
        print(*wardrobe.values())


    # 종류가 다르다면
    # (종류별 옷의 개수 + 1)을 모두 곱한 뒤 전혀 안입는 경우 -1
    # +1을 더하는 이유는 전혀 안입을 수도 있기 때문
    else :
        values = wardrobe.values()
        ans = 1
        for value in values :
            ans *= (value +1)

        print(ans-1)
