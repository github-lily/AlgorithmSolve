import sys

def main():
    input = sys.stdin.readline
    n = int(input().strip())
    cls = [list(map(int, input().split())) for _ in range(n)]  
    
    best_student = 0
    best_cnt = -1

    for i in range(n):
        same = [False] * n  
        for year in range(5):
            for j in range(n):
                if i == j:
                    continue
                if cls[i][year] == cls[j][year]:
                    same[j] = True  

        cnt = sum(same)
        if cnt > best_cnt:
            best_cnt = cnt
            best_student = i

    print(best_student + 1)  

if __name__ == "__main__":
    main()
