
import sys
input = sys.stdin.readline


# 2. 조합으로 남길 치킨집 구하기
# 이때, 현 치킨집 개수 = 남길 치킨집 개수 같으면 패스

def combination(M) :
    global L, chickens

    result = []
    def dfs(start,path) :
        if len(path) == M :
            result.append(path[:])
            return
        for i in range(start,L) :
            path.append(chickens[i])
            dfs(i+1, path)
            path.pop()

    dfs(0,[])
    return result        

# 3. 남은 치킨집과 집 좌표 저장, 치킨거리 계산
def cal(chickens_lst) :
    global ans, houses

    sum_val = 0
    for house in houses : 
        best = 99999
        for chicken in chickens_lst :
            dis = abs(chicken[0]-house[0]) + abs(chicken[1]-house[1])
            if best > dis :
                best = dis
        sum_val += best

# 4. 치킨거리 최소값 찾기
    if ans > sum_val :
        ans = sum_val

    return ans



# 0. 입력값받기
N,M = map(int,input().split())
city = [list(map(int,input().split())) for _ in range(N)]
ans = 99999


# 1. 탐색
# 1-1. 치킨집 좌표 저장
chickens = []

# 1-2. 집 좌표 저장
houses = []

for i in range(N) :
    for j in range(N) :
        if city[i][j] == 1 :
            houses.append((i+1,j+1))  # 좌표 1부터 시작
        elif city[i][j] == 2 :
            chickens.append((i+1,j+1))


L = len(chickens)
if L != M :
    for combi in combination(M) :
        cal(combi)
else :
    cal(chickens)



print(ans)