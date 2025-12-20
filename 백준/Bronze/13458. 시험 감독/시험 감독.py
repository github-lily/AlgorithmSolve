import sys

def main():
    input = sys.stdin.readline
    
    n = int(input().strip())
    a = list(map(int, input().split()))
    b, c = map(int, input().split())
    
    ans = 0
    for x in a:
        ans += 1  # 총감독관 1명
        rem = x - b
        if rem > 0:
            ans += (rem + c - 1) // c  # 부감독관 수(올림)
    
    print(ans)

if __name__ == "__main__":
    main()
