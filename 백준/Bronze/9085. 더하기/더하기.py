import sys

def main():
    input = sys.stdin.readline
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        nums = list(map(int, input().split()))
        print(sum(nums))

if __name__ == "__main__":
    main()
