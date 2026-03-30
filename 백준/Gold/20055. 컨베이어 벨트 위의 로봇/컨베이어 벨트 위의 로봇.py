# 0. 입력값
N,K = map(int,input().split())
size = N*2

durability = list(map(int,input().split()))
robot = [0] * size
stage = 0
s = 0       # 올리는 곳
e = N-1     # 내리는 곳

while True : 
    # 1. 벨트 한바퀴 회전
    s = (s-1) % size
    e = (e-1) % size
    stage += 1

    # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동(이동칸에 로봇이 없고, 내구도가 1 이상일 경우에만 이동)
    robot[e] = 0        # 로봇 내리기

    for i in range(N-1,0,-1) :
        cr = (s+i) % size
        if robot[cr] == 1 :
            # 로봇 있는지 & 내구도 확인
            nr = (cr+1) % size     # 다음칸 인덱스
            if robot[nr] == 0 : 
                if durability[nr] > 0 :
                    robot[nr] = 1       # 로봇 이동
                    robot[cr] = 0
                    durability[nr] -= 1     # 내구도 감소

    robot[e] = 0    # 이동 후 로봇 내리기
        
    # 3. 로봇 올리기 (내구도 1이상일 경우)
    if robot[s] == 0 and durability[s] > 0 :
        robot[s] = 1
        durability[s] -= 1

    # 4. 내구도가 0인 칸의 개수가 K개 이상이면 종료, 아니면 1번으로 이동 
    if durability.count(0) >= K :
        print(stage)
        break