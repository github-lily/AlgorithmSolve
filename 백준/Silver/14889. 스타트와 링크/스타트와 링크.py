import sys
input = sys.stdin.readline

N = int(input())
skills = [list(map(int,input().split())) for _ in range(N)]

players = [x for x in range(N)]
team_member = N//2


# 1) 조합으로 가능한 경우 찾기
def combinations(r) :
    global N
    result = []
    path = [0]      # 모든 경우에서 팀은 0이 있는 팀, 없는 팀으로 나뉨! team1, team2 상관없으므로 반만 탐색!
    def dfs(start) :
        if len(path) == r :
            result.append(path[:])
            return
        for i in range(start, N) :
            path.append(i)
            dfs(i+1)
            path.pop()
    dfs(1)          # 0은 이미 들어가있으므로 1부터 시작
    return result


# 2) 경우별 능력치 찾기
best_dif = 1000
for combi in combinations(team_member) :
    team1 = combi
    team2 = list(set(players) - set(combi))

    team1_power = 0
    team2_power = 0

    for i in range(team_member) :
        for j in range(i+1, team_member) :
            # ※서로서로의 능력치 더해주기(양방향)
            team1_power += skills[team1[i]][team1[j]] + skills[team1[j]][team1[i]]
            team2_power += skills[team2[i]][team2[j]] + skills[team2[j]][team2[i]]


# 3) 최소 차이 구하기
    dif = abs(team1_power - team2_power)

    if best_dif > dif :
        best_dif = dif
        if best_dif == 0 :
            break       # 0보다 작을 순 없음!


print(best_dif)

