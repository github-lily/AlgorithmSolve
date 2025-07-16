import sys

def main():
    total = 0
    for line in sys.stdin:
        n = int(line)
        if n == -1:
            break
        total += n
    print(total)

if __name__ == "__main__":
    main()
