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
    def dfs(start,path) :
        if len(path) == r :
            result.append(path[:])
            return
        for i in range(start, N) :
            path.append(i)
            dfs(i+1, path)
            path.pop()
    dfs(0,[])   
    return result

# 2) 경우별 능력치 찾기
best_dif = 1000
for combi in combinations(team_member) :
    min_dif = 1000
    team1 = combi
    team2 = list(set(players) - set(combi))

    team1_power = 0
    team2_power = 0

    for i in range(team_member) :
        for j in range(i+1, team_member) :
            # team1 힘의 합 구하기(※서로서로의 능력치 더해주기)
            team1_power += skills[team1[i]][team1[j]]
            team1_power += skills[team1[j]][team1[i]]

            team2_power += skills[team2[i]][team2[j]]
            team2_power += skills[team2[j]][team2[i]]


# 3) 최소 차이 구하기
    dif = abs(team1_power - team2_power)
    if min_dif > dif :
        min_dif = dif


    if best_dif > min_dif :
        best_dif = min_dif
    # print()

print(best_dif)




